#!/usr/bin/env python3
"""Office Joke Open entry.

Writes one single-line office joke to /output/entry.txt.
The gate requires UTF-8 text of 1 to 200 characters, not only
whitespace; the joke below is a single line, well under the cap.
No network, no secrets, no input files: the text is the entry.
"""

import os

JOKE = (
    "I hit reply-all to ask everyone to stop replying all, "
    "and 47 people replied all to agree."
)

def main() -> None:
    # The grader runs the program with /output as the artifact dir.
    # OUTPUT_DIR only exists so the entry can be test-run locally.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
