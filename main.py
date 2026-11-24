"""One Letter: Coffee or Tea -- make.fun entry.

The entry is exactly one letter: A for coffee, B for tea. This program
holds the letter A, checks it is a single letter with no word, explanation
or punctuation beside it, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LETTER = "A"

OUTPUT_PATH = "/output/entry.txt"


def check_letter(value):
    """The entry must be exactly one letter, A or B, and nothing else."""
    if not isinstance(value, str):
        raise ValueError("letter must be text")
    if len(value) != 1 or value not in ("A", "B"):
        raise ValueError("entry must be exactly one letter: A or B")
    return value


def main():
    letter = check_letter(LETTER)
    print(letter)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(letter + "\n")


if __name__ == "__main__":
    main()
