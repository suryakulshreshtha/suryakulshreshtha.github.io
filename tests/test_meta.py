"""Search snippets and link previews (LinkedIn, Slack, X, WhatsApp) have what they need."""
import json
import struct
from urllib.parse import urlparse

from conftest import fetch

CANONICAL = "https://suryakulshreshtha.github.io/"


def test_title_names_the_person_and_role(doc):
    assert doc.title.startswith("Surya Kulshreshtha")
    assert "SDET" in doc.title
    assert len(doc.title) <= 65   # keeps it from being cut off in search results


def test_description_fits_a_search_snippet(doc):
    assert 50 <= len(doc.meta["description"]) <= 160


def test_canonical_points_at_the_live_site(doc):
    assert doc.links["canonical"] == CANONICAL


def test_open_graph_tags(doc):
    m = doc.meta
    assert m["og:type"] == "website"
    assert m["og:url"] == CANONICAL
    assert m["og:title"].startswith("Surya Kulshreshtha")
    assert len(m["og:description"]) >= 50
    assert m["og:image"].startswith(CANONICAL)          # previews need an absolute https URL
    assert (m["og:image:width"], m["og:image:height"]) == ("1200", "630")
    assert m["og:image:alt"]


def test_twitter_card_tags(doc):
    m = doc.meta
    assert m["twitter:card"] == "summary_large_image"
    assert m["twitter:image"] == m["og:image"]
    assert m["twitter:title"] and m["twitter:description"] and m["twitter:image:alt"]


def test_preview_image_is_served_as_1200x630_png(doc, base_url):
    status, png = fetch(base_url + urlparse(doc.meta["og:image"]).path)
    assert status == 200
    assert png[:8] == b"\x89PNG\r\n\x1a\n"
    width, height = struct.unpack(">II", png[16:24])
    assert (width, height) == (1200, 630)
    assert len(png) < 1_000_000   # some preview bots ignore images over ~1 MB


def test_structured_data_describes_a_person(doc):
    assert len(doc.json_ld) == 1
    person = json.loads(doc.json_ld[0])
    assert person["@type"] == "Person"
    assert person["name"] == "Surya Kulshreshtha"
    assert person["url"] == CANONICAL
    assert "https://github.com/suryakulshreshtha" in person["sameAs"]


def test_robots_and_sitemap_are_served(base_url):
    _, robots = fetch(base_url + "/robots.txt")
    assert f"Sitemap: {CANONICAL}sitemap.xml" in robots.decode()
    _, sitemap = fetch(base_url + "/sitemap.xml")
    assert f"<loc>{CANONICAL}</loc>" in sitemap.decode()
