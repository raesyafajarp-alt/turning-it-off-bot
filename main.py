#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry bot.

Writes one single-line entry to entry.txt inside MAKEFUN_OUTPUT_DIR
(default /output). Deterministic, no network access.

The entry is exactly 123 characters on a single line, including the
em dash in "morning — I'm still buffering".
"""

import os
from pathlib import Path

ENTRY = (
    "Have you tried turning it off and on again? "
    "I tried it on myself this morning \u2014 "
    "I'm still buffering, but my hopes are high."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
