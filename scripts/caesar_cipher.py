
def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char

    return result


print("=== Caesar Cipher Tool ===")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_cipher(message, shift)
decrypted = caesar_cipher(encrypted, -shift)

print("\nEncrypted message:", encrypted)
print("Decrypted message:", decrypted)
