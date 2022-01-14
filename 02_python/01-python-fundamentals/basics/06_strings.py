"""
Demonstrates strings in Python.
Covers: slicing, methods, formatting, multiline, raw strings, encode/decode
"""

def caesar_cipher(text: str, shift: int, encrypt: bool = True) -> str:
    """A basic Caesar cipher encrypt/decrypt."""
    result = ""
    if not encrypt:
        shift = -shift
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def main():
    # Slicing and methods
    s = " Python Programming "
    print(f"Original: '{s}'")
    print(f"Stripped: '{s.strip()}'")
    print(f"Slicing [1:7]: '{s[1:7]}'")
    print(f"Replace: '{s.replace('Python', 'Cython')}'")
    print(f"Split: {s.split()}")
    print(f"Join: {'-'.join(['a', 'b', 'c'])}")

    # Multiline and raw strings
    multiline = """Line 1
Line 2
Line 3"""
    raw = r"C:\Users\Name"
    print(multiline)
    print(raw)

    # Encode/Decode
    utf8_encoded = "Hello World".encode("utf-8")
    print(f"Encoded: {utf8_encoded}")
    print(f"Decoded: {utf8_encoded.decode('utf-8')}")

    # Caesar Cipher
    original = "Hello, World!"
    encrypted = caesar_cipher(original, 3)
    decrypted = caesar_cipher(encrypted, 3, encrypt=False)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()
