"""Office Artifacts: The One-Line Placard Contest.

Writes a single-line museum placard for an ordinary office object,
treated as an ancient artifact, to /output/entry.txt.
"""

import os

PLACARD = (
    "Sticky note, yellow, c. 2003. Reads 'call me back' in an unknown hand; "
    "the call was never returned. Excavated from beneath a keyboard; "
    "donated by the night cleaner."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLACARD)


if __name__ == "__main__":
    main()
