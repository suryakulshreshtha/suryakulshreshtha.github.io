"""Page object for the terminal site."""
from __future__ import annotations

import re

from playwright.sync_api import Page, expect

ARMED = re.compile(r"\barmed\b")
DONE = re.compile(r"\bdone\b")


class Terminal:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.html = page.locator("html")
        self.main = page.locator("#term")
        self.blocks = page.locator("#term > .block")
        self.commands = page.locator("#term .prompt .cmd")
        self.skip_button = page.locator("#skip")
        self.final_prompt = page.locator("#final")
        self.test_count = page.locator("#test-count")
        self.test_dots = page.locator("#test-dots")
        self.ci_link = page.locator("#ci-link")
        self.links = page.locator("#term a[href]")

    def open(self, *, scripted: bool = True) -> "Terminal":
        self.page.goto("/")
        if scripted:
            expect(self.html).to_have_class(ARMED)
        return self

    def skip_animation(self) -> "Terminal":
        self.page.keyboard.press("Escape")
        return self.wait_until_done()

    def wait_until_done(self, timeout: float = 30_000) -> "Terminal":
        expect(self.html).to_have_class(DONE, timeout=timeout)
        return self

    def finished(self) -> "Terminal":
        return self.open().skip_animation()

    def text(self) -> str:
        return " ".join(self.main.inner_text().split())
