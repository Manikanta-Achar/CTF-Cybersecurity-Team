"""Display basic properties of an IPv4 or IPv6 address."""

import argparse
import ipaddress
from typing import Dict


def inspect_ip(value: str) -> Dict[str, object]:
    if not isinstance(value, str):
        raise TypeError("IP address must be a string")
    try:
        address = ipaddress.ip_address(value)
    except ValueError as exc:
        raise ValueError(f"invalid IP address: {value!r}") from exc

    return {
        "version": address.version,
        "address": str(address),
        "is_private": address.is_private,
        "is_global": address.is_global,
        "is_loopback": address.is_loopback,
        "is_link_local": address.is_link_local,
        "is_multicast": address.is_multicast,
        "is_reserved": address.is_reserved,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("address", help="IPv4 or IPv6 address")
    args = parser.parse_args()
    try:
        details = inspect_ip(args.address)
    except ValueError as exc:
        parser.error(str(exc))
    for name, value in details.items():
        print(f"{name}: {value}")


if __name__ == "__main__":
    main()
