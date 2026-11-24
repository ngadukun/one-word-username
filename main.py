"""One Word, One Username, One Reward - make.fun entry.

The brief asks for exactly one thing: my own make.fun username,
one word and nothing else. Writes it to output/entry.txt.
Python stdlib only, no network, fully deterministic.
"""

from pathlib import Path

ENTRY = "ngadukun"

OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "entry.txt"

MAX_CHARS = 30  # the brief caps the username at 30 characters


def check_entry(text: str) -> str:
    """Return the username unchanged, or raise if it breaks the brief."""
    if text != text.strip() or " " in text or "\n" in text:
        raise ValueError("the entry must be a single word, nothing else")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"username is {len(text)} chars, outside 1-{MAX_CHARS}")
    return text


def main() -> None:
    word = check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(word + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
