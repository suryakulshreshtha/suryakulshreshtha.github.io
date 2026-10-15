"""The terminal's `pytest -q` output is not decoration: it must match this suite."""
import pathlib
import re
import subprocess
import sys

from playwright.sync_api import expect

from pages import Terminal

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "ci.yml"


def collected_tests() -> int:
    """How many tests a plain `pytest` run executes (external link checks excluded)."""
    out = subprocess.run(
        [sys.executable, "-m", "pytest", "--collect-only", "-q", "-p", "no:cacheprovider"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    match = re.search(r"^(\d+)(?:/\d+)? tests? collected", out, re.MULTILINE)
    assert match, out
    return int(match.group(1))


def test_terminal_reports_the_real_test_count(page):
    term = Terminal(page).finished()
    total = collected_tests()
    expect(term.test_count).to_have_text(str(total))
    assert len(term.test_dots.text_content()) == total, "one dot per test, like real pytest -q"


def test_ci_badge_tracks_this_repos_workflow(page):
    term = Terminal(page).finished()
    assert WORKFLOW.is_file()
    assert re.search(r"^\s*run:.*\bpytest\b", WORKFLOW.read_text(), re.MULTILINE)
    expect(term.ci_link).to_have_attribute("href", re.compile(r"/actions/workflows/ci\.yml"))
    expect(term.ci_link.locator("img")).to_have_attribute(
        "src", re.compile(r"/actions/workflows/ci\.yml/badge\.svg"))
