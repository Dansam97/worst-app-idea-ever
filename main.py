#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — make.fun entry.

Writes one sentence (<=240 chars) pitching the worst, most useless app
imaginable to /output/entry.txt. Deterministic, no network, no dependencies.
"""

import os

ENTRY = (
    "SilenceWatch: an app that alerts you the moment your neighbor's dog "
    "stops barking, so you can finally worry about the quiet — $4.99 a "
    "month, or $49.99 a year for premium quiet with push notifications."
)


def _validate(text):
    """Defensive gate check: the entry must pass the sealed scorer's gate
    (UTF-8 text, 1-240 characters, not only whitespace, one line)."""
    if not text or not text.strip():
        raise ValueError("entry is blank")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 240:
        raise ValueError("entry exceeds the 240-character gate")


def main():
    _validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
