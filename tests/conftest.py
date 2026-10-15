"""Shared fixtures.

By default the suite serves this repo on a throwaway localhost port and stubs every
third-party request (Google Fonts, the CI badge), so it runs offline and gives the same
result every time. Set SITE_URL=https://suryakulshreshtha.github.io to point the same
tests at the deployed site instead (no stubs).
"""
from __future__ import annotations

import functools
import http.server
import os
import pathlib
import threading
import urllib.error
import urllib.request

import pytest
from playwright.sync_api import BrowserContext

from htmlscan import Scan, scan

ROOT = pathlib.Path(__file__).resolve().parents[1]
SITE_URL = os.environ.get("SITE_URL", "").rstrip("/")
_BADGE_STUB = b'<svg xmlns="http://www.w3.org/2000/svg" width="110" height="20"></svg>'


class _QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):  # keep pytest output clean
        pass


@pytest.fixture(scope="session")
def base_url() -> str:
    """Overrides pytest-base-url, so page.goto("/") hits the local copy (or SITE_URL)."""
    if SITE_URL:
        yield SITE_URL
        return
    handler = functools.partial(_QuietHandler, directory=str(ROOT))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{server.server_port}"
    server.shutdown()


def _keep_offline(ctx: BrowserContext, base_url: str) -> None:
    """Answer third-party requests with harmless stubs instead of the network."""
    if SITE_URL:
        return

    def handle(route):
        request = route.request
        if request.url.startswith(base_url):
            return route.continue_()
        if request.resource_type == "image":
            return route.fulfill(status=200, content_type="image/svg+xml", body=_BADGE_STUB)
        if request.resource_type == "stylesheet":
            return route.fulfill(status=200, content_type="text/css", body="")
        return route.fulfill(status=204, body="")

    ctx.route("**/*", handle)


@pytest.fixture
def context(context: BrowserContext, base_url: str) -> BrowserContext:
    """pytest-playwright's context, made hermetic."""
    _keep_offline(context, base_url)
    return context


@pytest.fixture
def new_context(browser, browser_context_args, base_url):
    """Factory for contexts with extra options (no JS, reduced motion, phone size...)."""
    made: list[BrowserContext] = []

    def make(**overrides) -> BrowserContext:
        ctx = browser.new_context(**{**browser_context_args, **overrides})
        _keep_offline(ctx, base_url)
        made.append(ctx)
        return ctx

    yield make
    for ctx in made:
        ctx.close()


def fetch(url: str) -> tuple[int, bytes]:
    """GET a URL; HTTP errors come back as a status code instead of an exception."""
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as err:
        return err.code, b""


@pytest.fixture(scope="session")
def raw_html(base_url: str) -> str:
    """The page exactly as served: what crawlers and link-preview bots receive."""
    status, body = fetch(base_url + "/")
    assert status == 200
    return body.decode("utf-8")


@pytest.fixture(scope="session")
def doc(raw_html: str) -> Scan:
    return scan(raw_html)
