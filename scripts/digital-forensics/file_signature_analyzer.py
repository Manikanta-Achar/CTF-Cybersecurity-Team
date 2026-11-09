"""Identify a small set of common file formats from their leading bytes."""

import argparse
from pathlib import Path
from typing import Dict, Union

SIGNATURES = (
    (b"\x89PNG\r\n\x1a\n", "PNG image"),
    (b"\xff\xd8\xff", "JPEG image"),
    (b"GIF87a", "GIF image"),
    (b"GIF89a", "GIF image"),
    (b"%PDF-", "PDF document"),
    (b"PK\x03\x04", "ZIP archive"),
    (b"\x1f\x8b", "GZIP archive"),
    (b"\x7fELF", "ELF executable"),
)


def identify_signature(header: bytes) -> str:
    if not isinstance(header, bytes):
        raise TypeError("header must be bytes")
    for signature, file_type in SIGNATURES:
        if header.startswith(signature):
            return file_type
    return "Unknown"


def analyze_file(path: Union[str, Path]) -> Dict[str, Union[str, int]]:
    with Path(path).open("rb") as file_handle:
        header = file_handle.read(16)
    return {
        "file": str(path),
        "size_bytes": Path(path).stat().st_size,
        "type": identify_signature(header),
        "header_hex": header.hex(" "),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="Path to a local file")
    args = parser.parse_args()
    try:
        details = analyze_file(args.file)
    except OSError as exc:
        parser.error(str(exc))
    for name, value in details.items():
        print(f"{name}: {value}")


if __name__ == "__main__":
    main()
