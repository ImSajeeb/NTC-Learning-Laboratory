"""Basic arithmetic helpers used in the number theory workshop."""


def is_divisible(a: int, b: int) -> bool:
    """Return True if b divides a."""
    if b == 0:
        raise ValueError("Divisor cannot be zero.")
    return a % b == 0


def positive_divisors(n: int):
    """Return all positive divisors of n."""
    value = abs(int(n))
    if value == 0:
        return [0]
    return [i for i in range(1, value + 1) if value % i == 0]


def prime_factorization(n: int):
    """Return the prime factors of n as a list."""
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


def factor_count(n: int) -> int:
    """Return the number of positive divisors of n."""
    return len(positive_divisors(n))


def sum_of_divisors(n: int) -> int:
    """Return the sum of positive divisors of n."""
    return sum(positive_divisors(n))


if __name__ == "__main__":
    print("Divisibility:", is_divisible(48, 6))
    print("Divisors of 36:", positive_divisors(36))
    print("Prime factorization of 60:", prime_factorization(60))
