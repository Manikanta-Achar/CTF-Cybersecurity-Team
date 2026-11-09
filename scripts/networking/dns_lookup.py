"""Resolve a hostname to IP addresses using the system resolver."""

import argparse
import socket
from typing import List


def lookup_addresses(hostname: str) -> List[str]:
    if not isinstance(hostname, str):
        raise TypeError("hostname must be a string")
    if not hostname or hostname != hostname.strip() or any(char.isspace() for char in hostname):
        raise ValueError("provide a non-empty hostname without whitespace")
    if "\0" in hostname:
        raise ValueError("hostname cannot contain a null character")
    results = {
        result[4][0]
        for result in socket.getaddrinfo(hostname, None, type=socket.SOCK_STREAM)
    }
    if not results:
        raise OSError(f"no IP addresses returned for {hostname!r}")
    return sorted(results)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("hostname", help="Hostname you are authorized to look up")
    args = parser.parse_args()
    try:
        addresses = lookup_addresses(args.hostname)
    except (OSError, ValueError) as exc:
        parser.error(f"lookup failed: {exc}")
    for address in addresses:
        print(address)


if __name__ == "__main__":
    main()
