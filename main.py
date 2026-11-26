#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Rejected Olympic Sports entry.

Writes one funny single-line rejected Olympic sport to /output/entry.txt.
Deterministic, standard library only, no network, no input.
"""

import os

LINE = (
    "Synchronized sighing: teams exhale in perfect unison "
    "while judges deduct points for anyone who actually feels better."
)


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
