"""The terminal boots, types, can be skipped, and adapts to the visitor."""
import pytest
from playwright.sync_api import expect

from pages import Terminal

GOOGLEBOT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"


def test_page_loads_cleanly(page):
    problems = []
    page.on("console", lambda m: m.type == "error" and problems.append(m.text))
    page.on("pageerror", lambda e: problems.append(str(e)))
    page.on("requestfailed", lambda r: problems.append(f"failed: {r.url}"))
    Terminal(page).finished()
    assert problems == []


def test_types_commands_then_settles(page):
    term = Terminal(page).open()
    first = term.commands.first
    page.wait_for_function(
        "() => { const t = document.querySelector('#term .cmd').textContent;"
        " return t.length > 0 && t.length < 'grep \"root\" /etc/group'.length; }"
    )
    assert 'grep "root" /etc/group'.startswith(first.text_content())
    expect(term.blocks.nth(1)).to_be_hidden()

    term.wait_until_done()
    expect(term.final_prompt).to_be_visible()
    expect(term.skip_button).to_be_hidden()
    expect(term.commands.nth(-2)).to_have_text("pytest -q")


def test_any_key_skips_the_animation(page):
    term = Terminal(page).open()
    expect(term.skip_button).to_be_visible()
    term.skip_animation()
    for i in range(term.blocks.count()):
        expect(term.blocks.nth(i)).to_be_visible()


def test_skip_button_skips_and_disappears(page):
    term = Terminal(page).open()
    term.skip_button.click()
    term.wait_until_done(timeout=2_000)
    expect(term.skip_button).to_be_hidden()
    expect(term.final_prompt).to_be_visible()


def test_a_script_error_mid_animation_still_shows_the_page(page, doc):
    # Break a DOM method the typing loop needs, as an old or odd browser might.
    page.add_init_script("Element.prototype.after = function () { throw new Error('boom'); };")
    term = Terminal(page).open()
    term.wait_until_done(timeout=5_000)
    for i in range(term.blocks.count()):
        expect(term.blocks.nth(i)).to_be_visible()
    expect(term.commands.first).to_have_text('grep "root" /etc/group')
    expect(term.links).to_have_count(len(doc.anchors))


def test_reduced_motion_shows_everything_at_once(new_context):
    page = new_context(reduced_motion="reduce").new_page()
    term = Terminal(page).open()
    term.wait_until_done(timeout=1_000)
    expect(term.skip_button).to_be_hidden()


def test_crawlers_get_the_finished_page(new_context):
    page = new_context(user_agent=GOOGLEBOT).new_page()
    term = Terminal(page).open()
    term.wait_until_done(timeout=1_000)
    expect(term.test_count).to_be_visible()


def test_no_sideways_scroll_on_a_phone(new_context):
    page = new_context(viewport={"width": 375, "height": 812}, is_mobile=True).new_page()
    Terminal(page).finished()
    overflow = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
    assert overflow <= 0


@pytest.mark.parametrize("scheme, background", [
    ("light", "rgb(238, 242, 246)"),
    ("dark", "rgb(13, 25, 38)"),
])
def test_follows_the_system_theme(page, scheme, background):
    page.emulate_media(color_scheme=scheme)
    Terminal(page).finished()
    assert page.evaluate("getComputedStyle(document.body).backgroundColor") == background
