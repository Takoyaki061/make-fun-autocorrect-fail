#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes one line (under 200 characters) to /output/entry.txt: a text to a
date where autocorrect turned the SLIT of a red dress into a SLUT.
"""

TEXT = "I can't wait to see you tonight, I'm wearing that red dress you like, the one with the slut"

# Gate self-check (from the first local grade: the entry was valid at 91 chars,
# but the program wrote blindly). Refuse to write an entry the sealed scorer
# would reject: 1-199 chars, a single line, not only whitespace, no trailing
# newline (a newline would count toward the 199 and change the judged bytes).
assert 1 <= len(TEXT) <= 199, f"entry is {len(TEXT)} chars, gate needs 1-199"
assert "\n" not in TEXT, "entry must be a single line"
assert TEXT.strip(), "entry must not be only whitespace"


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
