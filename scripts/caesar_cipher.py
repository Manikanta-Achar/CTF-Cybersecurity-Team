"""Interactive Caesar cipher for the English A-Z alphabet."""


def caesar_cipher(text: str, shift: int) -> str:
    """Shift ASCII English letters; leave other characters unchanged."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(shift, int) or isinstance(shift, bool):
        raise TypeError("shift must be an integer")

    result = []
    for char in text:
        if "A" <= char <= "Z":
            base = ord("A")
        elif "a" <= char <= "z":
            base = ord("a")
        else:
            result.append(char)
            continue
        result.append(chr((ord(char) - base + shift) % 26 + base))
    return "".join(result)


def main() -> None:
    print("=== Caesar Cipher Tool ===")
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter integer shift value: "))
    except ValueError as exc:
        raise SystemExit("Error: shift must be an integer.") from exc

    encrypted = caesar_cipher(message, shift)
    print(f"\nEncrypted message: {encrypted}")
    print(f"Decrypted message: {caesar_cipher(encrypted, -shift)}")


if __name__ == "__main__":
    main()
