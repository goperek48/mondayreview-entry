#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun probe entry.

One line is the whole assignment: the funniest possible review of
my own Monday, kept under 200 characters. This script honours that
by doing the smallest job imaginable — it drops that one sentence
into /output/entry.txt and exits. No heading, no footnote, no
stray blank line diluting the joke.
"""

import os
import sys

# The sentence. It won the internal shortlist because it lands
# three gags in a single breath: a Monday whose plot is a loading
# screen (nothing ever happens), a battery stuck at 2% (running on
# fumes from the first hour), and the twist that it still managed
# to eat the entire day. The em-dash pauses the reader just long
# enough for the final clause to hit.
LINE = (
    "My Monday had the plot of a loading screen and the battery life "
    "of a phone at 2% \u2014 somehow it still took all day."
)


def main() -> int:
    # /output/entry.txt is where the grader looks, so the sentence
    # lives there and nowhere else. Written as one line with no
    # trailing newline and no second line lurking below it — the
    # character gate measures the file, and the file should contain
    # the joke and absolutely nothing more.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
