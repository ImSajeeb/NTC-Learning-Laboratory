"""Educational RSA implementation for the workshop."""

import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for candidate in [
    ROOT,
    ROOT / "02_Prime_Number_Analysis",
    ROOT / "03_GCD_and_Diophantine_Equations",
    ROOT / "04_Modular_Systems",
]:
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

from euclidean_methods import gcd
from modular_operations import mod_inverse, mod_pow
from prime_tools import is_prime


def generate_prime(start: int = 50, end: int = 500) -> int:
    """Generate a prime number in the given range."""
    start = max(2, int(start))
    end = max(start, int(end))
    for candidate in range(start, end + 1):
        if is_prime(candidate):
            return candidate
    raise ValueError(f"No prime found in the range [{start}, {end}].")


def generate_rsa_keypair(prime_min: int = 50, prime_max: int = 500):
    """Generate a small RSA key pair for educational use."""
    primes = [value for value in range(max(2, prime_min), max(prime_min, prime_max) + 1) if is_prime(value)]
    if len(primes) < 2:
        raise ValueError(f'Not enough primes available in [{prime_min}, {prime_max}] for RSA demonstration.')

    p, q = random.sample(primes, 2)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    for e in [3, 5, 17, 257, 65537]:
        if gcd(e, phi_n) == 1:
            break
    else:
        e = 3
        while gcd(e, phi_n) != 1:
            e += 2

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


def string_to_int(message: str):
    """Convert a simple message string to a single numeric code."""
    return sum(ord(ch) * (256 ** i) for i, ch in enumerate(message))


if __name__ == "__main__":
    keys = generate_rsa_keypair(50, 200)
    print("Keys:", keys)
    message = 42
    ciphertext = rsa_encrypt(message, keys["e"], keys["n"])
    recovered = rsa_decrypt(ciphertext, keys["d"], keys["n"])
    print("Message:", message)
    print("Ciphertext:", ciphertext)
    print("Recovered:", recovered)
