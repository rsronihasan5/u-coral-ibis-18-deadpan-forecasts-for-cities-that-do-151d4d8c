#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist.

Writes a single one-line weather forecast for an invented city to
/output/entry.txt. The line is a fixed, authored forecast: absurd yet
delivered in the plain, confident tone of a TV meteorologist, with
concrete numbers and a specific recurring detail that make the invented
place feel real.
"""

import os
import shutil
import sys

ENTRY = (
    "In New Bumbershoot, expect 87 degrees and a 40% chance of rain "
    "that falls sideways, as it has done every Tuesday since 1987, "
    "so bring a second umbrella."
)


def main() -> None:
    out_dir = "/output"
    # Never remove the output directory itself; only clear its contents.
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        try:
            if os.path.isdir(path) and not os.path.islink(path):
                shutil.rmtree(path)
            else:
                os.unlink(path)
        except OSError:
            # A stale entry we cannot remove must not stop the forecast
            # from being written; leave it and carry on.
            continue
    line = ENTRY.strip()
    if not 1 <= len(line) <= 160:
        sys.exit("entry must be 1-160 characters")
    if not line.strip():
        sys.exit("entry must not be only whitespace")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
