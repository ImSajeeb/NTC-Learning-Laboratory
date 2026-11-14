# Viva Preparation

## Mathematical fundamentals

### What is Number Theory?
Number theory studies the properties of integers and their relationships, especially divisibility, primes, factorization, and modular arithmetic.

### What is divisibility?
A number $a$ divides $b$ if there exists an integer $k$ such that $b = ak$.

### What is a prime number?
A prime number is an integer greater than 1 with exactly two positive divisors: 1 and itself.

### What is GCD?
The greatest common divisor is the largest positive integer that divides both numbers.

### What is LCM?
The least common multiple is the smallest positive integer divisible by both numbers.

## Algorithms

### How does the Euclidean Algorithm work?
It repeatedly replaces the larger number by the remainder when divided by the smaller one until the remainder is zero. The last non-zero remainder is the GCD.

### What is the Extended Euclidean Algorithm?
It finds integers $x$ and $y$ such that $ax + by = gcd(a,b)$.

### What is modular arithmetic?
It studies arithmetic with remainders. We work with numbers modulo $m$.

### What is modular inverse?
A modular inverse of $a$ modulo $m$ is a number $x$ such that $ax \equiv 1 \pmod{m}$, when $gcd(a,m)=1$.

### How do we calculate Euler's Totient Function?
For $n$, the function counts integers from 1 to $n$ that are coprime to $n$.

## Theorems

### Fermat's Little Theorem
If $p$ is prime and $a$ is not divisible by $p$, then $a^{p-1} \equiv 1 \pmod{p}$.

### Euler's theorem
If $gcd(a,n)=1$, then $a^{\phi(n)} \equiv 1 \pmod{n}$.

### Chinese Remainder Theorem
It solves systems of congruences with pairwise coprime moduli.

## Cryptography

### What is plaintext?
Plaintext is the original readable message.

### What is ciphertext?
Ciphertext is the encrypted message.

### What is encryption?
Encryption converts plaintext into ciphertext using a key or mathematical rule.

### What is decryption?
Decryption reverses the process and recovers the original message.

### What is symmetric-key cryptography?
Both parties use the same secret key for encryption and decryption.

### What is public-key cryptography?
The public key is shared, while the private key remains secret. RSA is the classic example.

### How does RSA work?
RSA uses prime numbers, Euler's totient function, and modular exponentiation to build a public/private key pair.

### Why are prime numbers important in RSA?
RSA security depends on the difficulty of factoring $n = pq$ when $p$ and $q$ are large primes.

### Why is textbook RSA educational only?
It is not secure for real-world communication because it uses small parameters and lacks modern padding and key-management protections.

## Implementation questions

- How is the Euclidean Algorithm implemented in Python?
- How do we compute modular inverses?
- How does RSA key generation work?
- Why are assertions useful in testing cryptographic code?
- What are the edge cases for prime checking and modular inverses?

## Final viva advice

Focus on explaining the logic behind each algorithm, not just memorizing formulas. Show that you understand why each step is mathematically justified and how the Python code matches the mathematics.
