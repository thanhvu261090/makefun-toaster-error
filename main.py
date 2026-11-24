#!/usr/bin/env python3
"""make.fun entry: The Funniest Toaster Error Message.

Writes one line -- the error message a kitchen toaster shows its owner
when something goes wrong -- to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

# The entry: one line, at most 120 characters.
ENTRY = "ERROR: No bread detected. I toasted the air anyway. The air is ready."

MAX_LENGTH = 120


def gate_check(text):
    """Enforce the competition gate on the entry text.

    Returns True only if the text is valid UTF-8, 1 to 120 characters,
    not only whitespace, and a single line.
    """
    if not isinstance(text, str):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    if not 1 <= len(text) <= MAX_LENGTH:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    # No other control characters either: a real appliance display shows
    # printable text only.
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        return False
    return True


def main():
    if not gate_check(ENTRY):
        raise SystemExit("gate check failed: entry is not valid")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"{ENTRY} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
