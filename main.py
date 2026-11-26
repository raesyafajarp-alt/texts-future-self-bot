#!/usr/bin/env python3
"""Texts from Your Future Self — one funny text from future you.

Writes a single text message (< 200 chars) to /output/entry.txt.
The entry is a fixed string: deterministic, byte-identical on every run.
"""

import os

ENTRY = (
    "It's you from 2046. Whatever you do, DON'T eat the gas station "
    "sushi today. I'm typing this from a hospital bed. Also buy "
    "Bitcoin. But mostly: the sushi."
)


def validate_entry(text: str) -> None:
    """Gate: 1-200 chars, UTF-8, not only whitespace (per RULES.txt)."""
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry length {len(text)} outside 1..200 chars")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # raises if not encodable


def _write_entry(text: str, path: str = "/output/entry.txt") -> None:
    validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    _write_entry(ENTRY)


if __name__ == "__main__":
    main()
