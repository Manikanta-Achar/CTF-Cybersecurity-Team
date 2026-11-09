import tempfile
import unittest
from importlib import import_module
from pathlib import Path
from unittest.mock import patch

from scripts.caesar_cipher import caesar_cipher
from scripts.cryptography.base64_tool import decode_text, encode_text
from scripts.cryptography.sha256_tool import sha256_text
from scripts.networking.ip_information import inspect_ip
from scripts.networking.dns_lookup import lookup_addresses

file_hash_checker = import_module("scripts.digital-forensics.file_hash_checker")
file_signature_analyzer = import_module("scripts.digital-forensics.file_signature_analyzer")
sha256_file = file_hash_checker.sha256_file
validate_expected_hash = file_hash_checker.validate_expected_hash
analyze_file = file_signature_analyzer.analyze_file
identify_signature = file_signature_analyzer.identify_signature


class CaesarCipherTests(unittest.TestCase):
    def test_encrypt_decrypt_and_wrap(self):
        self.assertEqual(caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(caesar_cipher("Khoor, Zruog!", -3), "Hello, World!")
        self.assertEqual(caesar_cipher("Zz", 1), "Aa")

    def test_large_shifts_and_non_ascii(self):
        self.assertEqual(caesar_cipher("Aé!", 26), "Aé!")
        self.assertEqual(caesar_cipher("A", 27), "B")

    def test_rejects_invalid_arguments(self):
        with self.assertRaises(TypeError):
            caesar_cipher(3, 1)
        with self.assertRaises(TypeError):
            caesar_cipher("text", 1.5)


class Base64Tests(unittest.TestCase):
    def test_encode_decode_utf8_and_empty_text(self):
        self.assertEqual(encode_text("Hello, world!"), "SGVsbG8sIHdvcmxkIQ==")
        self.assertEqual(decode_text("SGVsbG8sIHdvcmxkIQ=="), "Hello, world!")
        self.assertEqual(decode_text(encode_text("café")), "café")
        self.assertEqual(encode_text(""), "")

    def test_rejects_invalid_base64_or_non_utf8(self):
        for value in ("not base64!", "YQ", "_w=="):
            with self.subTest(value=value), self.assertRaises(ValueError):
                decode_text(value)
        with self.assertRaises(TypeError):
            encode_text(123)


class HashTests(unittest.TestCase):
    def test_sha256_text(self):
        self.assertEqual(
            sha256_text("abc"),
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
        )
        self.assertEqual(len(sha256_text("")), 64)

    def test_file_hash_and_expected_hash_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "sample.txt"
            file_path.write_bytes(b"abc")
            digest = sha256_file(file_path)
            self.assertEqual(digest, sha256_text("abc"))
            self.assertEqual(validate_expected_hash(digest.upper()), digest)
            with self.assertRaises(ValueError):
                validate_expected_hash("not-a-hash")
            with self.assertRaises(FileNotFoundError):
                sha256_file(Path(directory) / "missing.txt")


class FileSignatureTests(unittest.TestCase):
    def test_known_unknown_and_empty_headers(self):
        self.assertEqual(identify_signature(b"\x89PNG\r\n\x1a\nrest"), "PNG image")
        self.assertEqual(identify_signature(b"%PDF-1.7"), "PDF document")
        self.assertEqual(identify_signature(b""), "Unknown")
        self.assertEqual(identify_signature(b"plain text"), "Unknown")
        with self.assertRaises(TypeError):
            identify_signature("not bytes")

    def test_file_analysis_and_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "sample.bin"
            file_path.write_bytes(b"\x1f\x8bdata")
            result = analyze_file(file_path)
            self.assertEqual(result["size_bytes"], 6)
            self.assertEqual(result["type"], "GZIP archive")
            with self.assertRaises(FileNotFoundError):
                analyze_file(Path(directory) / "missing.bin")


class IpInformationTests(unittest.TestCase):
    def test_ipv4_and_ipv6_properties(self):
        self.assertTrue(inspect_ip("127.0.0.1")["is_loopback"])
        self.assertTrue(inspect_ip("192.168.1.1")["is_private"])
        ipv6 = inspect_ip("2001:4860:4860::8888")
        self.assertEqual(ipv6["version"], 6)
        self.assertEqual(ipv6["address"], "2001:4860:4860::8888")

    def test_rejects_invalid_address(self):
        with self.assertRaises(ValueError):
            inspect_ip("localhost")


class DnsLookupTests(unittest.TestCase):
    def test_rejects_invalid_hostname_before_network_access(self):
        for hostname in ("", " example.com", "example com", "a\0b"):
            with self.subTest(hostname=hostname), self.assertRaises(ValueError):
                lookup_addresses(hostname)

    @patch("scripts.networking.dns_lookup.socket.getaddrinfo", return_value=[])
    def test_empty_resolver_result_is_an_error(self, _getaddrinfo):
        with self.assertRaises(OSError):
            lookup_addresses("example.invalid")

    def test_localhost_resolves(self):
        addresses = lookup_addresses("localhost")
        self.assertTrue(addresses)
        self.assertEqual(addresses, sorted(set(addresses)))


if __name__ == "__main__":
    unittest.main()
