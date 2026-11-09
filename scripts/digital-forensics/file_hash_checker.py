"""Calculate and optionally verify the SHA-256 hash of a local file."""

import argparse
import hashlib
import re
from pathlib import Path
from typing import Union


def sha256_file(path: Union[str, Path]) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as file_handle:
        for chunk in iter(lambda: file_handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_expected_hash(expected: str) -> str:
    if not isinstance(expected, str) or re.fullmatch(r"[0-9a-fA-F]{64}", expected) is None:
        raise ValueError("expected SHA-256 must contain exactly 64 hexadecimal characters")
    return expected.lower()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="Path to a local file")
    parser.add_argument("--expected", help="Optional expected SHA-256 digest to compare")
    args = parser.parse_args()
    try:
        expected = validate_expected_hash(args.expected) if args.expected is not None else None
        digest = sha256_file(args.file)
        print(f"SHA-256: {digest}")
        if expected is not None:
            print(f"Match: {digest == expected}")
    except (OSError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
