"""Basic modular arithmetic and inverse functions."""

from src.number_theory import extended_gcd


def mod_add(a: int, b: int, m: int) -> int:
    """Return (a + b) mod m."""
    if m <= 0:
        raise ValueError("Modulus must be positive.")
    return (a % m + b % m) % m


def mod_sub(a: int, b: int, m: int) -> int:
    """Return (a - b) mod m."""
    if m <= 0:
        raise ValueError("Modulus must be positive.")
    return (a % m - b % m) % m


def mod_mul(a: int, b: int, m: int) -> int:
    """Return (a * b) mod m."""
    if m <= 0:
        raise ValueError("Modulus must be positive.")
    return (a % m * b % m) % m


def mod_pow(base: int, exponent: int, m: int) -> int:
    """Compute base^exponent mod m using repeated squaring."""
    if m <= 0:
        raise ValueError("Modulus must be positive.")
    result = 1 % m
    base %= m
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % m
        base = (base * base) % m
        exponent >>= 1
    return result


def mod_inverse(a: int, m: int) -> int:
    """Return the inverse of a modulo m when gcd(a, m) = 1."""
    if m <= 0:
        raise ValueError("Modulus must be positive.")
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse for {a} modulo {m} because gcd(a, m) != 1.")
    return x % m


if __name__ == "__main__":
    print("(7+5) mod 11 =", mod_add(7, 5, 11))
    print("(7-5) mod 11 =", mod_sub(7, 5, 11))
    print("(7*5) mod 11 =", mod_mul(7, 5, 11))
    print("2^10 mod 13 =", mod_pow(2, 10, 13))
    print("inverse of 3 mod 11 =", mod_inverse(3, 11))
