# Mathematical Notes

## 1. Divisibility

If $a$ divides $b$, then there exists an integer $k$ such that $b = ak$.

This idea is fundamental because prime factorization, GCD, LCM, and modular arithmetic all depend on divisibility.

## 2. Prime Numbers

A prime number is an integer greater than 1 whose only positive divisors are 1 and itself. Examples: 2, 3, 5, 7, 11.

## 3. Greatest Common Divisor

The GCD is the largest positive integer that divides both numbers.

$$
gcd(a,b) = gcd(b, a \bmod b)
$$

This identity is the basis of the Euclidean Algorithm.

## 4. Modular Arithmetic

Two integers are congruent modulo $m$ if they differ by a multiple of $m$:

$$
a \equiv b \pmod{m}
$$

This is used heavily in cryptography and number theory.

## 5. Euler's Totient Function

For a positive integer $n$,

$$
\phi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)
$$

This counts how many integers from 1 to $n$ are relatively prime to $n$.

## 6. Fermat's Little Theorem

If $p$ is prime and $a$ is not divisible by $p$, then:

$$
a^{p-1} \equiv 1 \pmod{p}
$$

## 7. Euler's Theorem

If $\gcd(a,n)=1$, then:

$$
a^{\phi(n)} \equiv 1 \pmod{n}
$$

## 8. Chinese Remainder Theorem

If $m_1, m_2, \dots, m_k$ are pairwise coprime, then the system

$$
x \equiv a_i \pmod{m_i}
$$

has a unique solution modulo $M = m_1 m_2 \cdots m_k$.

## 9. RSA Concept

RSA relies on the difficulty of factoring large products of primes. The public key is $(e,n)$ and the private key is $(d,n)$.

The decryption step is:

$$
m \equiv c^d \pmod{n}
$$

where $c \equiv m^e \pmod{n}$.

## Worked Example

If $p=5$ and $q=11$, then:

$$
n = 55, \quad \phi(n) = 4 \cdot 10 = 40
$$

Choose $e = 3$, since $\gcd(3,40)=1$. Then solve:

$$
3d \equiv 1 \pmod{40}
$$

We get $d = 27$.

This is a small educational RSA example.
