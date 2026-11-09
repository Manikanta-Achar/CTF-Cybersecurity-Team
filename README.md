# CTF Cybersecurity Team

A small, hands-on learning repository for a student team preparing for Capture The Flag competitions. It contains beginner-friendly Python utilities, reusable practice writeup templates, and curated starting points for continued learning. The tools are educational and are not a substitute for dedicated security software.

## Team

The repository lists Manikanta, Hithest Narayan A, and HemanthKumar H M as team members. The only profile link currently provided is [Manikanta-Achar](https://github.com/Manikanta-Achar); no profiles are guessed for other members. See [team information](team/README.md).

## Implemented tools

| Area | Tool | Purpose |
|---|---|---|
| Cryptography | Caesar Cipher | Shift English A-Z characters; preserve other characters. |
| Cryptography | Base64 Tool | Encode/decode UTF-8 text (encoding is not encryption). |
| Cryptography | SHA-256 Text Tool | Print the SHA-256 digest of supplied text. |
| Networking | DNS Lookup | Resolve a hostname through the system resolver. Use only for authorized lookups. |
| Networking | IP Information | Display basic `ipaddress` properties for an IPv4 or IPv6 address. |
| Digital forensics | File Hash Checker | Calculate SHA-256 for a local file and optionally compare an expected digest. |
| Digital forensics | File Signature Analyzer | Identify selected formats from file-header bytes; this is a basic hint, not proof of file safety or authenticity. |

## Requirements and setup

Python 3.8 or newer is recommended. All tools use the Python standard library; no third-party packages are required. From the repository root, no installation step is needed. Verify Python is available:

```powershell
python --version
```

If `python` is not on `PATH` in Windows, try `py --version` and replace `python` with `py` in the commands below.

## Quick start

Run commands from the repository root:

```powershell
python scripts\caesar_cipher.py
python scripts\cryptography\base64_tool.py encode "Hello, world!"
python scripts\cryptography\base64_tool.py decode "SGVsbG8sIHdvcmxkIQ=="
python scripts\cryptography\sha256_tool.py abc
python scripts\networking\dns_lookup.py localhost
python scripts\networking\ip_information.py 127.0.0.1
python scripts\digital-forensics\file_hash_checker.py .\README.md
python scripts\digital-forensics\file_signature_analyzer.py .\README.md
```

The Caesar Cipher is interactive. Example: input `Hello, World!` and shift `3` prints `Khoor, Zruog!`, then decrypts it back to `Hello, World!`. Other deterministic examples:

```text
Base64 encode "Hello, world!" -> SGVsbG8sIHdvcmxkIQ==
SHA-256 of "abc" -> ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
IP information for 127.0.0.1 -> version: 4; is_loopback: True
```

DNS results depend on the machine's configured resolver and network. File-analysis output depends on the selected local file.

## Tests

Run the unit tests from the repository root:

```powershell
python -m unittest discover -s tests -v
```

The tests cover normal and invalid inputs, edge cases, local temporary files, and a localhost resolver lookup.

## Repository structure

```text
team/                         Team information
writeups/                     Practice templates by CTF category
scripts/                      Small Python command-line tools
  cryptography/
  networking/
  digital-forensics/
tests/                        unittest coverage
resources/                    Learning links and guidance
```

## Writeups and responsible use

The five category folders under [writeups/](writeups/README.md) contain practice templates, not claimed challenge solutions. Add a flag only after solving a genuine challenge, and follow the event's disclosure rules. Use networking utilities only for authorized learning targets; the DNS tool makes a normal resolver query and does not scan or attack a host. For forensics tools, select files you are authorized to examine.

## Technologies and learning objectives

Python 3, the standard library, Git, and GitHub. Practice includes string transformations, encoding, hashing, DNS resolution, IP address parsing, binary file headers, input validation, testing, and clear technical documentation.
