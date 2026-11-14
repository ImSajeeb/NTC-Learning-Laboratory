"""Educational cryptography helpers for classical ciphers and RSA."""

import math

from src.modular_arithmetic import mod_inverse, mod_pow
from src.number_theory import gcd, is_prime


def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt text using the Caesar cipher."""
    result = []
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            letter_index = ord(ch) - base
            result.append(chr((letter_index + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypt text using the Caesar cipher."""
    return caesar_encrypt(text, -shift)


def affine_encrypt(text: str, a: int, b: int) -> str:
    """Encrypt text with the affine cipher y = a*x + b mod 26."""
    if math.gcd(a, 26) != 1:
        raise ValueError("The key a must be coprime with 26.")

    result = []
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            x = ord(ch) - base
            y = (a * x + b) % 26
            result.append(chr(y + base))
        else:
            result.append(ch)
    return "".join(result)


def affine_decrypt(text: str, a: int, b: int) -> str:
    """Decrypt text with the affine cipher."""
    if math.gcd(a, 26) != 1:
        raise ValueError("The key a must be coprime with 26.")

    inv_a = pow(a, -1, 26)
    result = []
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            y = ord(ch) - base
            x = ((y - b) * inv_a) % 26
            result.append(chr(x + base))
        else:
            result.append(ch)
    return "".join(result)


def generate_rsa_keypair(min_prime: int = 50, max_prime: int = 200):
    """Generate a small RSA key pair for educational use."""
    primes = [value for value in range(max(2, min_prime), max_prime + 1) if is_prime(value)]
    if len(primes) < 2:
        raise ValueError("Not enough primes exist in the chosen range.")

    import random

    p, q = random.sample(primes, 2)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    candidates = [3, 5, 17, 257, 65537]
    e = next((value for value in candidates if gcd(value, phi_n) == 1), None)
    if e is None:
        e = 3
        while gcd(e, phi_n) != 1:
            e += 2
            if e >= phi_n:
                raise ValueError("Could not find a valid RSA exponent in the chosen range.")

    d = mod_inverse(e, phi_n)
    return {
        "p": p,
        "q": q,
        "n": n,
        "phi_n": phi_n,
        "e": e,
        "d": d,
    }


def rsa_encrypt(message: int, e: int, n: int) -> int:
    """Encrypt a message integer using RSA."""
    if not (0 <= message < n):
        raise ValueError("For this educational example, message must satisfy 0 <= message < n.")
    return mod_pow(message, e, n)


def rsa_decrypt(ciphertext: int, d: int, n: int) -> int:
    """Decrypt a ciphertext integer using RSA."""
    if not (0 <= ciphertext < n):
        raise ValueError("Ciphertext must be a valid residue modulo n.")
    return mod_pow(ciphertext, d, n)


def string_to_int(message: str) -> int:
    """Convert a string to a simple integer representation."""
    total = 0
    for index, ch in enumerate(message):
        total += ord(ch) * (256 ** index)
    return total


if __name__ == "__main__":
    print("Caesar encryption:", caesar_encrypt("HELLO", 3))
    print("Caesar decryption:", caesar_decrypt("KHOOR", 3))
    print("Affine encryption:", affine_encrypt("NUMBER", 5, 8))
    print("Affine decryption:", affine_decrypt(affine_encrypt("NUMBER", 5, 8), 5, 8))
    keys = generate_rsa_keypair(50, 200)
    print("RSA keys:", keys)
    message = 42
    ciphertext = rsa_encrypt(message, keys["e"], keys["n"])
    print("Ciphertext:", ciphertext)
    print("Recovered:", rsa_decrypt(ciphertext, keys["d"], keys["n"]))
