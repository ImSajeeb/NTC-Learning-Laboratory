"""Prime-related utilities for the workshop."""


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


def primes_up_to(limit: int):
    """Generate all prime numbers less than or equal to limit."""
    if limit < 2:
        return []
    primes = []
    for candidate in range(2, limit + 1):
        if is_prime(candidate):
            primes.append(candidate)
    return primes


def prime_factorization(n: int):
    """Return the prime decomposition of n."""
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


if __name__ == "__main__":
    print("is_prime(17):", is_prime(17))
    print("is_prime(25):", is_prime(25))
    print("primes_up_to(30):", primes_up_to(30))
    print("Prime factors of 84:", prime_factorization(84))
