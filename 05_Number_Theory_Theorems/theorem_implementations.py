"""Number theory theorem helpers and CRT implementation."""

import sys
from math import prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOD_DIR = ROOT / "04_Modular_Systems"
if str(MOD_DIR) not in sys.path:
    sys.path.insert(0, str(MOD_DIR))

from modular_operations import mod_inverse


def euler_totient(n: int) -> int:
    """Compute the Euler totient function phi(n)."""
    if n <= 0:
        raise ValueError("n must be a positive integer.")

    value = n
    result = n
    p = 2
    while p * p <= value:
        if value % p == 0:
            while value % p == 0:
                value //= p
            result -= result // p
        p += 1 if p == 2 else 2
    if value > 1:
        result -= result // value
    return result


def fermat_little_theorem_valid(a: int, p: int) -> bool:
    """Check whether Fermat's Little Theorem holds for a and prime p."""
    if p <= 1:
        raise ValueError("p must be a prime integer greater than 1.")
    if a % p == 0:
        return True
    return (a ** (p - 1)) % p == 1


def euler_theorem_valid(a: int, n: int) -> bool:
    """Check Euler's theorem for coprime a and n."""
    if n <= 0:
        raise ValueError("n must be positive.")
    if a % n == 0:
        return False
    return (a ** euler_totient(n)) % n == 1


def chinese_remainder_theorem(congruences):
    """Solve a system of congruences x ≡ a_i (mod m_i) using CRT."""
    if not congruences:
        raise ValueError("At least one congruence is required.")

    mod_product = prod(mod for _, mod in congruences)
    result = 0

    for remainder, mod in congruences:
        if mod <= 0:
            raise ValueError("All moduli must be positive.")
        partial = mod_product // mod
        inverse = mod_inverse(partial, mod)
        result = (result + remainder * partial * inverse) % mod_product

    return result, mod_product


if __name__ == "__main__":
    print("phi(12) =", euler_totient(12))
    print("FLT valid for 2 mod 5:", fermat_little_theorem_valid(2, 5))
    print("Euler valid for 2 mod 9:", euler_theorem_valid(2, 9))
    print("CRT example:", chinese_remainder_theorem([(2, 3), (3, 5)]))
