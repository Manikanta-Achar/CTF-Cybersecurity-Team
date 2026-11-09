"""Encode and decode UTF-8 text with Base64."""

import argparse
import base64
import binascii


def encode_text(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return base64.b64encode(text.encode("utf-8")).decode("ascii")


def decode_text(encoded: str) -> str:
    if not isinstance(encoded, str):
        raise TypeError("encoded value must be a string")
    try:
        decoded = base64.b64decode(encoded.encode("ascii"), validate=True)
        return decoded.decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError, binascii.Error) as exc:
        raise ValueError("input must be valid Base64 containing UTF-8 text") from exc


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("encode", "decode"))
    parser.add_argument("text", help="Text to encode or Base64 text to decode")
    args = parser.parse_args()
    try:
        result = encode_text(args.text) if args.mode == "encode" else decode_text(args.text)
    except ValueError as exc:
        parser.error(str(exc))
    print(result)


if __name__ == "__main__":
    main()
