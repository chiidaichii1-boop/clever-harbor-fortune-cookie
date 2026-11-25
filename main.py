#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune cookie line for a crypto trader who was just
liquidated, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only. Never deletes the output directory.
"""

import os

ENTRY = "Beware of false friends. Your stop-loss was one of them."
# Verified: 56 characters, 10 words (gate: 1-160 chars, <=20 words).
# Determinism: two runs byte-identical,
# sha256 of entry.txt = 4ac32f9893c8fcbfd0e455167377ccb9510f67ffb9c22326bb98497b86648c83.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 160, "entry must be 1-160 characters"
    assert len(text.split()) <= 20, "entry must be at most 20 words"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
