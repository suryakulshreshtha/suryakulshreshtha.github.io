"""Links are safe, local files exist, and (with -m external) every outside link is alive."""
import pathlib
from urllib.parse import urlparse

import pytest

from conftest import fetch
from htmlscan import scan

SITE_HOST = "suryakulshreshtha.github.io"
INDEX = pathlib.Path(__file__).resolve().parents[1] / "index.html"
# Read at collection time so each outside link becomes its own test case.
EXTERNAL = sorted({
    a["href"] for a in scan(INDEX.read_text(encoding="utf-8")).anchors
    if a["href"].startswith("http") and urlparse(a["href"]).hostname != SITE_HOST
})
BROWSER_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Safari/537.36"


def test_new_tab_links_cannot_touch_the_opener(doc):
    for a in doc.anchors:
        if a.get("target") == "_blank":
            assert "noopener" in a.get("rel", "").split(), a["href"]


def test_own_site_references_resolve(doc, base_url):
    refs = [a["href"] for a in doc.anchors] + [i["src"] for i in doc.images]
    refs += list(doc.links.values()) + [v for k, v in doc.meta.items() if k.endswith(":image")]
    own = {urlparse(r).path or "/" for r in refs
           if urlparse(r).hostname in (None, SITE_HOST) and not r.startswith(("data:", "#", "mailto:"))}
    assert own, "expected at least the canonical URL and preview image"
    for path in sorted(own):
        status, _ = fetch(base_url + path)
        assert status == 200, path


@pytest.mark.external
@pytest.mark.parametrize("url", EXTERNAL)
def test_external_link_is_alive(playwright, url):
    api = playwright.request.new_context(user_agent=BROWSER_UA)
    try:
        status = api.get(url, timeout=20_000, max_redirects=10).status
    finally:
        api.dispose()
    if urlparse(url).hostname.endswith("linkedin.com"):
        assert status in (200, 999), status   # LinkedIn answers bots with 999
    else:
        assert status < 400, status
