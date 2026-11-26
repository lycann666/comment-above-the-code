#!/usr/bin/env python3
"""The Comment Above the Code — make.fun entry.

Writes one funny, painfully honest comment about fragile legacy code
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

# The line below is the entry itself and must stay byte-identical:
# no trailing newline is written, so entry.txt is exactly 104 bytes.
LINE = "// Changing line 42 breaks checkout, login, and one printer in accounting. We do not ask why anymore."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
