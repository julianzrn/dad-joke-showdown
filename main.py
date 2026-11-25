"""Entry for make.fun's "Dad Joke Showdown".

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

SETUP = "I used to hate doing laundry, but I've finally come clean about it. "
GROAN = "Same with these jokes, according to nobody in my family, ever."

ENTRY = SETUP + GROAN

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry line to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
