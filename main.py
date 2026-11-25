#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry program.

Writes exactly two lines to /output/entry.txt: line one warns the writer's
past self about one specific moment in a single sentence; line two says in
one sentence why that moment mattered and what changed because of it.

The program is fully deterministic: it writes the same bytes on every run.
The entry text is fixed in this file, so the two graded runs produce an
identical artifact.
"""

import os
from pathlib import Path

# The entry: 209 characters including newlines, two lines, each one sentence.
ENTRY = (
    "Don't throw away the letter from Diponegoro on 14 March 2019 \u2014 "
    "open it; it is an acceptance, not a rejection.\n"
    "It sat in the bin for a week, and by the time you fished it out, "
    "your place had gone to someone else.\n"
)


def main() -> None:
    # The grader runs this in a sandbox where /output exists; the override
    # exists only so the entry can be verified locally. It is read as data.
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
