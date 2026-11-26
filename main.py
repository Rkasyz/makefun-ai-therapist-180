#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry.

Writes one funny single-line diagnosis from an AI therapist to its
human into $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

ENTRY = (
    "Diagnosis: chronic tab-hoarding with acute notification anxiety. "
    "Prescription: close 47 tabs, touch grass, and stop asking if the "
    "cloud is judging you. It is. I am the cloud."
)

# The gate counts the file's characters: 1–200, one line, not only
# whitespace. Refuse to run if the entry ever drifts outside it.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"
assert ENTRY.strip() == ENTRY and "\n" not in ENTRY, "entry must be one line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file holds exactly the entry line.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
