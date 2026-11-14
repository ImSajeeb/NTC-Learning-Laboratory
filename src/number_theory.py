"""Compact number theory utilities for the assignment."""


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b."""
    x, y = abs(int(a)), abs(int(b))
    while y:
        x, y = y, x % y
    return x


def extended_gcd(a: int, b: int):
    """Return (g, x, y) such that ax + by = gcd(a, b)."""
    a = int(a)
    b = int(b)
    if a == 0 and b == 0:
        raise ValueError("gcd(0, 0) is undefined.")

    old_r, r = abs(a), abs(b)
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    if a < 0:
        old_s = -old_s
    if b < 0:
        old_t = -old_t

    return old_r, old_s, old_t


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of a and b."""
    a = int(a)
    b = int(b)
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def is_prime(n: int) -> bool:
    """Return True if n is prime."""
    value = int(n)
    if value <= 1:
        return False
    if value in (2, 3):
        return True
    if value % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def prime_factorization(n: int):
    """Return the prime factors of n using trial division."""
    value = abs(int(n))
    if value < 2:
        return []

    factors = []
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors.append(divisor)
            value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return factors


def primes_up_to(limit: int):
    """Return all prime numbers up to limit."""
    if limit < 2:
        return []
    return [value for value in range(2, limit + 1) if is_prime(value)]


def euler_totient(n: int) -> int:
    """Calculate Euler's totient function phi(n)."""
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
    """Check Fermat's little theorem for a and prime p."""
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
    """Solve x ≡ a_i (mod m_i) using the Chinese Remainder Theorem."""
    if not congruences:
        raise ValueError("At least one congruence is required.")

    from math import prod
    from src.modular_arithmetic import mod_inverse

    mod_product = prod(mod for _, mod in congruences)
    result = 0

    for remainder, mod in congruences:
        if mod <= 0:
            raise ValueError("All moduli must be positive.")
        partial = mod_product // mod
        inv = mod_inverse(partial, mod)
        result = (result + remainder * partial * inv) % mod_product

    return result, mod_product


if __name__ == "__main__":
    print("gcd(48, 18) =", gcd(48, 18))
    print("lcm(12, 18) =", lcm(12, 18))
    print("is_prime(17) =", is_prime(17))
    print("prime_factorization(60) =", prime_factorization(60))
    print("phi(12) =", euler_totient(12))
    print("CRT example =", chinese_remainder_theorem([(2, 3), (3, 5)]))
