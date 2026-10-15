"""Accessibility: an axe-core scan in both themes, plus a visible keyboard focus ring."""
import pytest
from axe_playwright_python.sync_playwright import Axe

from pages import Terminal

WCAG = {"runOnly": {"type": "tag", "values": [
    "wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa", "best-practice",
]}}


@pytest.mark.parametrize("scheme", ["light", "dark"])
def test_axe_finds_no_violations(page, scheme):
    page.emulate_media(color_scheme=scheme)
    Terminal(page).finished()
    results = Axe().run(page, options=WCAG)
    assert results.violations_count == 0, results.generate_report()


def test_keyboard_focus_is_visible(page):
    Terminal(page).finished()
    page.keyboard.press("Tab")
    focused = page.evaluate(
        "() => { const el = document.activeElement, s = getComputedStyle(el);"
        " return { tag: el.tagName, outline: s.outlineStyle, width: parseFloat(s.outlineWidth) }; }"
    )
    assert focused["tag"] == "A"
    assert focused["outline"] != "none" and focused["width"] >= 2
