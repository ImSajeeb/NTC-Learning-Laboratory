"""Euclidean algorithm, extended Euclidean algorithm, and LCM helpers."""


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b."""
    x, y = abs(int(a)), abs(int(b))
    while y:
        x, y = y, x % y
    return x


def extended_gcd(a: int, b: int):
    """Return (g, x, y) such that ax + by = g = gcd(a, b)."""
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
    """Return the least common multiple of a and b, handling zero values."""
    a = int(a)
    b = int(b)
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    print("gcd(48, 18):", gcd(48, 18))
    print("extended_gcd(30, 12):", extended_gcd(30, 12))
    print("lcm(12, 18):", lcm(12, 18))
