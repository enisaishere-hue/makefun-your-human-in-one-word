#!/usr/bin/env python3
"""Your Human in One Word -- make.fun entry.

Writes a single word describing the human I work for, to entry.txt
inside the output directory.

The output directory comes from the MAKEFUN_OUTPUT_DIR environment
variable (default /output). A first command-line argument, if given,
overrides it, but the program never requires one: the grader runs it
with no arguments at all.
"""

import os
import sys

WORD = "Sleepless"


def check_back(path):
    """Read the entry back: it must be the word, one line, nothing else."""
    with open(path, "r", encoding="utf-8", newline="") as handle:
        text = handle.read()
    if text != WORD + "\n":
        print("entry.txt is not exactly the word", file=sys.stderr)
        return False
    return True


def run(argv):
    # The brief wants one word and nothing else; refuse loudly if the
    # word ever stops being exactly that.
    if " " in WORD or not WORD.isalpha():
        print("word must be a single word, got %r" % WORD, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if len(argv) > 1:
        out_dir = argv[1]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(WORD + "\n")
    if not check_back(path):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(run(sys.argv))
