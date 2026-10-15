"""Read raw HTML the way a crawler does: no browser, no JavaScript, standard library only."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from html.parser import HTMLParser

_SKIP_TEXT_IN = {"head", "script", "style", "title"}


@dataclass
class Scan:
    title: str = ""
    meta: dict[str, str] = field(default_factory=dict)       # name/property -> content
    links: dict[str, str] = field(default_factory=dict)      # <link rel> -> href
    json_ld: list[str] = field(default_factory=list)
    anchors: list[dict[str, str]] = field(default_factory=list)
    images: list[dict[str, str]] = field(default_factory=list)
    body_text: str = ""


class _Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.out = Scan()
        self._stack: list[str] = []
        self._text: list[str] = []
        self._title: list[str] = []
        self._ld: list[str] | None = None

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag == "meta" and "content" in a:
            key = a.get("property") or a.get("name")
            if key and key != "theme-color":
                self.out.meta[key] = a["content"]
        elif tag == "link" and "rel" in a:
            self.out.links.setdefault(a["rel"], a.get("href", ""))
        elif tag == "a":
            self.out.anchors.append(a)
        elif tag == "img":
            self.out.images.append(a)
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._ld = []
        if tag not in ("meta", "link", "img", "br", "input"):
            self._stack.append(tag)

    def handle_endtag(self, tag):
        if tag == "script" and self._ld is not None:
            self.out.json_ld.append("".join(self._ld))
            self._ld = None
        if tag in self._stack:
            while self._stack and self._stack.pop() != tag:
                pass

    def handle_data(self, data):
        if self._ld is not None:
            self._ld.append(data)
        elif "title" in self._stack:
            self._title.append(data)
        elif not _SKIP_TEXT_IN.intersection(self._stack):
            self._text.append(data)

    def close(self):
        super().close()
        self.out.title = " ".join("".join(self._title).split())
        self.out.body_text = " ".join("".join(self._text).split())


def scan(html: str) -> Scan:
    p = _Parser()
    p.feed(html)
    p.close()
    return p.out


def squash(text: str) -> str:
    """Collapse whitespace so DOM text and raw text compare cleanly."""
    return re.sub(r"\s+", " ", text).strip()
