"""Regenerate the two images in this repo.

    og.png               link-preview card, rendered from scripts/og-card.html (1200x630)
    docs/screenshot.png  the finished terminal, dark theme, for the README

Usage:  python scripts/capture.py            (needs Playwright + Chromium, see README)
"""
from __future__ import annotations

import functools
import http.server
import pathlib
import threading

from playwright.sync_api import BrowserContext, sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def main(on_context=None) -> None:
    """on_context(ctx) lets a caller add request routing (e.g. local fonts when offline)."""
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(_Quiet, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_port}"

    with sync_playwright() as p:
        browser = p.chromium.launch()

        def context(**kw) -> BrowserContext:
            ctx = browser.new_context(**kw)
            if on_context:
                on_context(ctx)
            return ctx

        card = context(viewport={"width": 1200, "height": 630}).new_page()
        card.goto(f"{base}/scripts/og-card.html")
        card.evaluate("document.fonts.ready.then(() => true)")
        card.screenshot(path=ROOT / "og.png")

        shot = context(viewport={"width": 1100, "height": 760}, color_scheme="dark",
                       reduced_motion="reduce", device_scale_factor=1.5).new_page()
        shot.goto(f"{base}/")
        shot.evaluate("document.fonts.ready.then(() => true)")
        (ROOT / "docs").mkdir(exist_ok=True)
        shot.screenshot(path=ROOT / "docs" / "screenshot.png", full_page=True)

        browser.close()
    server.shutdown()
    print("wrote og.png and docs/screenshot.png")


if __name__ == "__main__":
    main()
