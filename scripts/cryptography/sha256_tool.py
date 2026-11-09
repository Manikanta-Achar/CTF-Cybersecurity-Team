"""Generate a SHA-256 digest for text."""

import argparse
import hashlib


def sha256_text(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text", help="Text to hash")
    args = parser.parse_args()
    print(sha256_text(args.text))


if __name__ == "__main__":
    main()
