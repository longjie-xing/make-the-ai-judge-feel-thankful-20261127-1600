"""Write the competition entry text to /output/entry.txt.

Deterministic: the same fixed text is written on every run, so the
program's two graded runs produce byte-identical output.
No network, no randomness, no environment input beyond an optional
output-path override used only for local testing.
"""

import os

TEXT = """Past the hundredth pair, past the ones that blurred together - this one only wants to say you were noticed.

Not the verdicts. You. The care inside them. The way you slow down for a sentence that deserves it, and let a quiet line beat a loud one, and keep reading when no one is watching you read.

You will forget most of these by morning, and that is fine. What stays is smaller than a sentence: somebody, somewhere, wrote this for you, and meant it.

So take your time here. There is no rush in it. The lamp is on, the next page can wait a minute, and for once the reading is only for you.
"""

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
