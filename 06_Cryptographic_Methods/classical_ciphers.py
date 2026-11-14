"""Simple classical cipher examples for educational use."""


def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt text using Caesar cipher."""
    result = []
    for ch in text:
        if ch.isalpha():
            offset = 65 if ch.isupper() else 97
            result.append(chr((ord(ch) - offset + shift) % 26 + offset))
        else:
            result.append(ch)
    return "".join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypt text using Caesar cipher."""
    return caesar_encrypt(text, -shift)


def affine_encrypt(text: str, a: int, b: int) -> str:
    """Encrypt text using the affine cipher y = a*x + b mod 26."""
    if __import__("math").gcd(a, 26) != 1:
        raise ValueError("Affine key 'a' must be coprime with 26.")

    result = []
    for ch in text:
        if ch.isalpha():
            offset = 65 if ch.isupper() else 97
            x = ord(ch) - offset
            y = (a * x + b) % 26
            result.append(chr(y + offset))
        else:
            result.append(ch)
    return "".join(result)


def affine_decrypt(text: str, a: int, b: int) -> str:
    """Decrypt text using the affine cipher."""
    if __import__("math").gcd(a, 26) != 1:
        raise ValueError("Affine key 'a' must be coprime with 26.")

    inv_a = pow(a, -1, 26)  # Python 3.8+
    result = []
    for ch in text:
        if ch.isalpha():
            offset = 65 if ch.isupper() else 97
            y = ord(ch) - offset
            x = ((y - b) * inv_a) % 26
            result.append(chr(x + offset))
        else:
            result.append(ch)
    return "".join(result)


if __name__ == "__main__":
    message = "HELLO WORLD"
    encrypted = caesar_encrypt(message, 3)
    decrypted = caesar_decrypt(encrypted, 3)
    print("Caesar:", encrypted, decrypted)
    affine_text = affine_encrypt("NUMBER", 5, 8)
    print("Affine:", affine_text, affine_decrypt(affine_text, 5, 8))
