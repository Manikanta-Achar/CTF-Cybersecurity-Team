# Python Practice Tools

These small command-line programs demonstrate Python fundamentals through CTF-relevant, benign tasks. They use only Python's standard library and are intended for learning—not as security or malware-analysis products.

## Tools and commands

Run commands from the repository root in PowerShell:

| Tool | Command | Example result |
|---|---|---|
| Caesar Cipher | `python scripts\caesar_cipher.py` | Input `HELLO`, shift `3` -> `KHOOR`; decrypts to `HELLO`. |
| Base64 encode | `python scripts\cryptography\base64_tool.py encode "Hello, world!"` | `SGVsbG8sIHdvcmxkIQ==` |
| Base64 decode | `python scripts\cryptography\base64_tool.py decode "SGVsbG8sIHdvcmxkIQ=="` | `Hello, world!` |
| SHA-256 text | `python scripts\cryptography\sha256_tool.py abc` | `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad` |
| DNS lookup | `python scripts\networking\dns_lookup.py localhost` | Prints addresses returned by the local system resolver. |
| IP information | `python scripts\networking\ip_information.py 127.0.0.1` | Includes `version: 4` and `is_loopback: True`. |
| Local file hash | `python scripts\digital-forensics\file_hash_checker.py .\README.md` | Prints the file's SHA-256 digest. |
| File hash compare | `python scripts\digital-forensics\file_hash_checker.py .\README.md --expected <64-hex-digest>` | Prints `Match: True` or `Match: False`. |
| File signature | `python scripts\digital-forensics\file_signature_analyzer.py .\README.md` | Reports `Unknown` for text unless it begins with a recognized signature. |

If `python` is unavailable in Windows, use the Python launcher `py` in its place. Base64 is an encoding, not encryption. The signature analyzer recognizes only a short list of file headers; an unknown result does not imply a file is safe, and a known signature does not establish authenticity.

## Implementation notes

- The Caesar tool shifts ASCII English letters and preserves punctuation and non-ASCII characters.
- The Base64 tool accepts UTF-8 text and rejects malformed Base64 or decoded non-UTF-8 data.
- SHA-256 tools hash UTF-8 text or stream local files in chunks.
- DNS lookup uses the operating system resolver; use only for authorized lookups.
- IP information uses Python's `ipaddress` module and does not send network traffic.
- Forensics tools read only the local file path supplied by the user.

## Tests

From the repository root:

```powershell
python -m unittest discover -s tests -v
```

The tests use temporary sample files and a localhost lookup; no third-party packages are needed.
