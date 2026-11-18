<h1 align="center">NTC Learning Laboratory</h1>
<h3 align="center">Number Theory and Cryptography Workshop</h3>

<p align="center">
  <b>A Python-Based Academic Project on Number Theory, Mathematical Algorithms, and Cryptography</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue.svg" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/Project-Academic-green.svg" alt="Project Academic">
  <img src="https://img.shields.io/badge/Domain-Number%20Theory-orange.svg" alt="Domain Number Theory">
  <img src="https://img.shields.io/badge/Domain-Cryptography-red.svg" alt="Domain Cryptography">
  <img src="https://img.shields.io/badge/Platform-Google%20Colab-yellow.svg" alt="Platform Google Colab">
</p>

---

## 1. Introduction

The **NTC Learning Laboratory** is an educational Python project designed to explore the mathematical foundations of Number Theory and their applications in Cryptography.

Number Theory is a branch of mathematics that studies integers, prime numbers, divisibility, modular arithmetic, and relationships between numbers. These mathematical concepts form the foundation of many cryptographic algorithms, including RSA.

This project combines mathematical theory with practical Python implementations. It provides algorithms, Jupyter notebooks, computational experiments, and documentation to help students understand how mathematical concepts work in real-world computational applications.

The project covers seven major areas:
1. Mathematical Foundations
2. Prime Number Analysis
3. GCD and Diophantine Equations
4. Modular Arithmetic
5. Number Theory Theorems
6. Classical Cryptography
7. Public-Key Cryptography (RSA)

The main objective is to connect mathematical definitions, theorem statements, algorithmic implementations, and cryptographic applications.

---

## 2. Project Information

| Field | Details |
| :--- | :--- |
| **Project Name** | NTC Learning Laboratory |
| **Project Title** | Number Theory and Cryptography Workshop |
| **Student** | Md. Sajeeb Khan |
| **Student ID** | IT23032 |
| **Department** | Information and Communication Technology |
| **University** | Mawlana Bhashani Science and Technology University |
| **Programming Language** | Python |
| **Development Environment** | VS Code, Jupyter Notebook, Google Colab |
| **Project Type** | Academic and Educational |

---

## 3. Project Objectives

The major objectives are:
- Understand the mathematical foundations of Number Theory.
- Implement divisibility and prime factorization algorithms.
- Understand the Euclidean and Extended Euclidean Algorithms.
- Solve basic linear Diophantine equations.
- Perform modular arithmetic operations.
- Understand and implement important number theory theorems.
- Explore the Chinese Remainder Theorem.
- Implement classical encryption and decryption algorithms.
- Understand the mathematical foundation of RSA.
- Verify mathematical properties using Python.
- Develop practical programming skills through computational experiments.

---

## 4. Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python** | Algorithm implementation |
| **NumPy** | Numerical computation |
| **Matplotlib** | Visualization and diagrams |
| **Jupyter Notebook** | Interactive mathematical experiments |
| **Google Colab** | Cloud-based execution |
| **Git and GitHub** | Version control and project hosting |

---

## 5. Repository Structure

```text
NTC-Learning-Laboratory/
│
├── 01_Mathematical_Foundations/
│   ├── __init__.py
│   ├── arithmetic_operations.py
│   └── mathematical_concepts.ipynb
│
├── 02_Prime_Number_Analysis/
│   ├── __init__.py
│   ├── prime_tools.py
│   └── prime_number_exploration.ipynb
│
├── 03_GCD_and_Diophantine_Equations/
│   ├── __init__.py
│   ├── euclidean_methods.py
│   └── gcd_experiments.ipynb
│
├── 04_Modular_Systems/
│   ├── __init__.py
│   ├── modular_operations.py
│   └── modular_arithmetic.ipynb
│
├── 05_Number_Theory_Theorems/
│   ├── __init__.py
│   ├── theorem_implementations.py
│   └── fermat_euler_crt.ipynb
│
├── 06_Cryptographic_Methods/
│   ├── __init__.py
│   ├── classical_ciphers.py
│   └── cryptography_fundamentals.ipynb
│
├── 07_Public_Key_Cryptography/
│   ├── __init__.py
│   ├── rsa_engine.py
│   └── rsa_algorithm_explained.ipynb
│
├── documentation/
│   ├── mathematical_notes.md
│   ├── references.md
│   ├── viva_preparation.md
│   └── viva_questions.md
│
├── experiments/
│   ├── algorithm_verification.ipynb
│   └── computational_observations.ipynb
│
├── figures/
│
├── notebooks/
│   ├── 01_Number_Theory.ipynb
│   ├── 02_Modular_Arithmetic.ipynb
│   ├── 03_Number_Theory_Algorithms.ipynb
│   ├── 04_Cryptography.ipynb
│   └── 05_RSA_Implementation.ipynb
│
├── src/
│   ├── __init__.py
│   ├── cryptography.py
│   ├── modular_arithmetic.py
│   └── number_theory.py
│
├── generate_diagrams.py
├── validate_repo.py
├── debug_validate.py
├── requirements.txt
└── README.md
```

---

## 6. Mathematical Foundations

### 6.1 Divisibility
An integer $a$ divides an integer $b$ if there exists an integer $k$ such that:
$$b = ak$$

It is represented by:
$$a \mid b$$

**Example:**
$$6 \mid 48$$
Because:
$$48 = 6 \times 8$$

However:
$$5 \nmid 48$$
because $48$ cannot be expressed as an integer multiple of $5$.

**Python implementation:**
```python
def is_divisible(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero.")
    return a % b == 0

print(is_divisible(48, 6))
print(is_divisible(48, 5))
```

**Output:**
```text
True
False
```

### 6.2 Prime Numbers
A prime number is a positive integer greater than $1$ that has exactly two positive divisors: $1$ and itself.

**Examples:**
$$2, 3, 5, 7, 11, 13, 17, 19$$

A number that has more than two positive divisors is called a composite number.

**Python implementation:**
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for number in range(1, 21):
    if is_prime(number):
        print(number, end=" ")
```

**Output:**
```text
2 3 5 7 11 13 17 19
```

### 6.3 Fundamental Theorem of Arithmetic
Every integer greater than $1$ can be expressed uniquely as a product of prime numbers, apart from the order of the factors.

**Mathematically:**
$$n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$$
where each $p_i$ is a distinct prime number.

**Example:**
$$60 = 2^2 \times 3 \times 5$$

**Python implementation:**
```python
def prime_factorization(n):
    if n < 2:
        raise ValueError("n must be greater than 1.")
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors

print(prime_factorization(60))
```

**Output:**
```text
[2, 2, 3, 5]
```

---

## 7. GCD and Diophantine Equations

### 7.1 Greatest Common Divisor (GCD)
The Greatest Common Divisor of two integers is the largest positive integer that divides both numbers.

**Example:**
$$\gcd(48, 18) = 6$$

The common divisors are:
$$1, 2, 3, 6$$
Therefore, the GCD is $6$.

### 7.2 Euclidean Algorithm
The Euclidean Algorithm calculates the GCD using repeated division.

The mathematical identity is:
$$\gcd(a, b) = \gcd(b, a \bmod b)$$

The process continues until the remainder becomes zero.

**Example:**
$$48 = 18 \times 2 + 12$$
$$18 = 12 \times 1 + 6$$
$$12 = 6 \times 2 + 0$$
Therefore:
$$\gcd(48, 18) = 6$$

**Python implementation:**
```python
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 18))
```

**Output:**
```text
6
```

### 7.3 Extended Euclidean Algorithm
The Extended Euclidean Algorithm finds three integers $g, x, y$ satisfying:
$$ax + by = g$$
where:
$$g = \gcd(a, b)$$
This identity is known as **Bézout's Identity**.

**Example:**
For $a = 30$ and $b = 12$:
$$30(1) + 12(-2) = 6$$
Therefore:
$$x = 1, \quad y = -2, \quad g = 6$$

**Python implementation:**
```python
def extended_gcd(a, b):
    if a == 0 and b == 0:
        raise ValueError("gcd(0, 0) is undefined.")
    old_r, r = abs(a), abs(b)
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if a < 0:
        old_s = -old_s
    if b < 0:
        old_t = -old_t
    return old_r, old_s, old_t

print(extended_gcd(30, 12))
```

**Output:**
```text
(6, 1, -2)
```

### 7.4 Least Common Multiple (LCM)
The Least Common Multiple is the smallest positive integer divisible by both given nonzero integers.

**Formula:**
$$\operatorname{lcm}(a, b) = \frac{|a \times b|}{\gcd(a, b)}$$

**Example:**
$$\operatorname{lcm}(12, 18) = 36$$

**Python implementation:**
```python
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

print(lcm(12, 18))
```

**Output:**
```text
36
```

### 7.5 Linear Diophantine Equation
A linear Diophantine equation has the form:
$$ax + by = c$$
where $a, b, c, x, y$ are integers.

**Existence condition:**
An integer solution exists if and only if:
$$\gcd(a, b) \mid c$$

**Example:**
$$6x + 9y = 3$$
Since $\gcd(6, 9) = 3$ and $3 \mid 3$, integer solutions exist.
One solution is:
$$x = 2, \quad y = -1$$
because:
$$6(2) + 9(-1) = 3$$

---

## 8. Modular Arithmetic

### 8.1 Modular Congruence
Two integers $a$ and $b$ are congruent modulo $m$ if their difference is divisible by $m$:
$$a \equiv b \pmod{m}$$

**Equivalent condition:**
$$m \mid (a - b)$$

**Example:**
$$17 \equiv 5 \pmod{12}$$
Because:
$$17 - 5 = 12$$

### 8.2 Modular Addition
$$(a + b) \bmod m$$
**Example:** $(7 + 5) \bmod 11 = 1$

```python
def mod_add(a, b, m):
    if m <= 0:
        raise ValueError("Modulus must be positive.")
    return (a + b) % m

print(mod_add(7, 5, 11))
```

### 8.3 Modular Subtraction
$$(a - b) \bmod m$$
**Example:** $(7 - 5) \bmod 11 = 2$

```python
def mod_sub(a, b, m):
    if m <= 0:
        raise ValueError("Modulus must be positive.")
    return (a - b) % m

print(mod_sub(7, 5, 11))
```

### 8.4 Modular Multiplication
$$(a \times b) \bmod m$$
**Example:** $(7 \times 5) \bmod 11 = 2$

```python
def mod_mul(a, b, m):
    if m <= 0:
        raise ValueError("Modulus must be positive.")
    return (a * b) % m

print(mod_mul(7, 5, 11))
```

### 8.5 Modular Exponentiation
$$a^b \bmod m$$
**Example:** $2^{10} \bmod 13 = 10$

**Python implementation:**
```python
def mod_pow(a, b, m):
    if m <= 0:
        raise ValueError("Modulus must be positive.")
    if b < 0:
        raise ValueError("Exponent must be non-negative.")
    return pow(a, b, m)

print(mod_pow(2, 10, 13))
```

### 8.6 Modular Multiplicative Inverse
The modular inverse of $a$ modulo $m$ is an integer $x$ satisfying:
$$ax \equiv 1 \pmod{m}$$

The inverse exists if and only if:
$$\gcd(a, m) = 1$$

**Example:**
$$3 \times 4 = 12, \quad 12 \bmod 11 = 1$$
Therefore:
$$3^{-1} \equiv 4 \pmod{11}$$

**Python implementation:**
```python
from math import gcd

def mod_inverse(a, m):
    if m <= 1:
        raise ValueError("Modulus must be greater than 1.")
    if gcd(a, m) != 1:
        raise ValueError("Modular inverse does not exist.")
    return pow(a, -1, m)

print(mod_inverse(3, 11))
```

**Output:**
```text
4
```

---

## 9. Number Theory Theorems

This section is one of the most important parts of the project. It demonstrates how number theory theorems can be translated into Python algorithms and computationally verified.

The following four major topics are implemented:
1. Euler's Totient Function
2. Fermat's Little Theorem
3. Euler's Theorem
4. Chinese Remainder Theorem

### 9.1 Euler's Totient Function

#### Definition
Euler's Totient Function, represented by $\varphi(n)$, counts the number of positive integers less than or equal to $n$ that are relatively prime to $n$. Two integers are relatively prime if their greatest common divisor is $1$.

**Mathematically:**
$$\varphi(n) = |\{k : 1 \le k \le n, \gcd(k, n) = 1\}|$$

#### Formula
If the distinct prime factors of $n$ are $p_1, p_2, \dots, p_k$, then:
$$\varphi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)$$

#### Example: Calculate $\varphi(12)$
Prime factorization:
$$12 = 2^2 \times 3$$

Therefore:
$$\varphi(12) = 12\left(1 - \frac{1}{2}\right)\left(1 - \frac{1}{3}\right) = 12 \times \frac{1}{2} \times \frac{2}{3} = 4$$

The positive integers from $1$ to $12$ that are relatively prime to $12$ are:
$$1, 5, 7, 11$$
There are four such integers.

#### Python implementation
```python
def euler_totient(n):
    if n <= 0:
        raise ValueError("n must be positive.")
    result = n
    value = n
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

print("phi(12) =", euler_totient(12))
print("phi(10) =", euler_totient(10))
print("phi(15) =", euler_totient(15))
```

**Output:**
```text
phi(12) = 4
phi(10) = 4
phi(15) = 8
```

#### Applications
Euler's Totient Function is important in:
- RSA public-key cryptography.
- Calculating the size of the multiplicative group modulo $n$.
- Modular arithmetic.
- Euler's theorem.
- Understanding multiplicative inverses.

#### Time Complexity
The implementation uses trial division and requires approximately $O(\sqrt{n})$ divisor checks in the worst case.

---

### 9.2 Fermat's Little Theorem

#### Statement
Fermat's Little Theorem states that if $p$ is a prime number and $a$ is an integer relatively prime to $p$, then:
$$a^{p-1} \equiv 1 \pmod{p}$$

**The conditions are:**
1. $p$ must be prime.
2. $a$ must not be divisible by $p$.
3. Therefore, $\gcd(a, p) = 1$.

#### Example
Let $a = 2, p = 5$. According to Fermat's Little Theorem:
$$2^{5-1} \equiv 1 \pmod{5}$$
$$2^4 = 16, \quad 16 \bmod 5 = 1$$
Therefore:
$$2^4 \equiv 1 \pmod{5}$$
The theorem is verified.

#### Python implementation
```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def fermat_little_theorem_valid(a, p):
    if not is_prime(p):
        raise ValueError("p must be prime.")
    if gcd(a, p) != 1:
        return False
    return pow(a, p - 1, p) == 1

print(fermat_little_theorem_valid(2, 5))
print(fermat_little_theorem_valid(3, 7))
```

**Output:**
```text
True
True
```

#### Explanation of the Code
- First, the function checks whether $p$ is prime.
- Next, it checks whether $a$ and $p$ are relatively prime.
- It calculates the modular exponentiation using Python's built-in `pow()` function.
- Finally, it checks whether the result equals $1$.

#### Applications
- Prime number testing.
- Modular arithmetic.
- RSA mathematical foundations.
- Modular inverse calculations.

> **Important Note:** Fermat's Little Theorem provides a necessary mathematical property for primes, but passing a single Fermat test does not prove that an arbitrary number is prime. Composite numbers (such as Carmichael numbers) can sometimes pass Fermat tests.

---

### 9.3 Euler's Theorem

#### Statement
Euler's theorem generalizes Fermat's Little Theorem. It states that if $a$ and $n$ are relatively prime, then:
$$a^{\varphi(n)} \equiv 1 \pmod{n}$$

The required condition is:
$$\gcd(a, n) = 1$$

#### Example
Let $a = 2, n = 9$. First calculate:
$$\varphi(9) = 9\left(1 - \frac{1}{3}\right) = 6$$

According to Euler's theorem:
$$2^6 \equiv 1 \pmod{9}$$
Calculate:
$$2^6 = 64, \quad 64 \bmod 9 = 1$$
Therefore:
$$2^6 \equiv 1 \pmod{9}$$

#### Python implementation
```python
def euler_theorem_valid(a, n):
    if n <= 0:
        raise ValueError("n must be positive.")
    if gcd(a, n) != 1:
        return False
    phi = euler_totient(n)
    return pow(a, phi, n) == 1

print(euler_theorem_valid(2, 9))
print(euler_theorem_valid(3, 10))
```

**Output:**
```text
True
True
```

#### Explanation
1. Calculate the GCD of $a$ and $n$.
2. Check whether the GCD is $1$.
3. Calculate Euler's Totient Function $\varphi(n)$.
4. Compute $a^{\varphi(n)} \bmod n$.
5. Verify that the result equals $1$.

#### Applications
- RSA encryption and decryption.
- Modular exponentiation.
- Number theory.
- Cryptographic key construction.

---

### 9.4 Chinese Remainder Theorem (CRT)

#### Statement
The Chinese Remainder Theorem states that if the moduli $m_1, m_2, \dots, m_k$ are pairwise relatively prime, then the system of congruences:
$$\begin{aligned}
x &\equiv a_1 \pmod{m_1} \\
x &\equiv a_2 \pmod{m_2} \\
&\;\;\vdots \\
x &\equiv a_k \pmod{m_k}
\end{aligned}$$
has a unique solution modulo:
$$M = m_1 m_2 \cdots m_k$$

#### Example
Solve:
$$x \equiv 2 \pmod{3}$$
$$x \equiv 3 \pmod{5}$$

1. **Calculate combined modulus:**
   $$M = 3 \times 5 = 15$$
2. **Calculate partial products:**
   $$M_1 = \frac{15}{3} = 5, \quad M_2 = \frac{15}{5} = 3$$
3. **Find modular inverses:**
   $$5^{-1} \equiv 2 \pmod{3}$$
   $$3^{-1} \equiv 2 \pmod{5}$$
4. **Apply the CRT formula:**
   $$x = \sum_{i=1}^{k} a_i M_i y_i \pmod{M}$$
   $$x = (2 \times 5 \times 2) + (3 \times 3 \times 2) = 20 + 18 = 38$$
   $$x = 38 \bmod 15 = 8 \pmod{15}$$

**Verification:**
- $8 \bmod 3 = 2$
- $8 \bmod 5 = 3$

Both conditions are satisfied.

#### Python implementation
```python
from math import gcd, prod

def chinese_remainder_theorem(congruences):
    if not congruences:
        raise ValueError("At least one congruence is required.")
    for remainder, modulus in congruences:
        if modulus <= 0:
            raise ValueError("Moduli must be positive.")
    moduli = [m for _, m in congruences]
    # Verify pairwise coprimality
    for i in range(len(moduli)):
        for j in range(i + 1, len(moduli)):
            if gcd(moduli[i], moduli[j]) != 1:
                raise ValueError("Moduli must be pairwise coprime.")
    M = prod(moduli)
    result = 0
    for remainder, modulus in congruences:
        partial = M // modulus
        inverse = pow(partial, -1, modulus)
        result += remainder * partial * inverse
    return result % M, M

solution, combined_modulus = chinese_remainder_theorem([
    (2, 3),
    (3, 5)
])
print("Solution:", solution)
print("Combined modulus:", combined_modulus)
```

**Output:**
```text
Solution: 8
Combined modulus: 15
```

#### Applications
- Cryptographic computation.
- RSA optimization.
- Modular equation solving.
- Computer arithmetic.
- Number-theoretic algorithms.

---

### 9.5 Complete Number Theory Theorem Implementation

The following is the recommended corrected version of the project's theorem module.

**File:** `05_Number_Theory_Theorems/theorem_implementations.py`

```python
"""Number theory theorem implementations."""
from math import gcd, prod


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def euler_totient(n):
    """Calculate Euler's phi function."""
    if n <= 0:
        raise ValueError("n must be positive.")
    result = n
    value = n
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


def fermat_little_theorem_valid(a, p):
    """Verify Fermat's Little Theorem."""
    if not is_prime(p):
        raise ValueError("p must be prime.")
    if gcd(a, p) != 1:
        return False
    return pow(a, p - 1, p) == 1


def euler_theorem_valid(a, n):
    """Verify Euler's theorem."""
    if n <= 0:
        raise ValueError("n must be positive.")
    if gcd(a, n) != 1:
        return False
    phi = euler_totient(n)
    return pow(a, phi, n) == 1


def chinese_remainder_theorem(congruences):
    """Solve pairwise coprime modular congruences."""
    if not congruences:
        raise ValueError("At least one congruence is required.")
    moduli = [m for _, m in congruences]
    if any(m <= 0 for m in moduli):
        raise ValueError("Moduli must be positive.")
    for i in range(len(moduli)):
        for j in range(i + 1, len(moduli)):
            if gcd(moduli[i], moduli[j]) != 1:
                raise ValueError("Moduli must be pairwise coprime.")
    M = prod(moduli)
    result = 0
    for remainder, modulus in congruences:
        partial = M // modulus
        inverse = pow(partial, -1, modulus)
        result += remainder * partial * inverse
    return result % M, M


if __name__ == "__main__":
    print("Euler Totient Function:")
    print("phi(12) =", euler_totient(12))
    print("\nFermat's Little Theorem:")
    print(fermat_little_theorem_valid(2, 5))
    print("\nEuler's Theorem:")
    print(euler_theorem_valid(2, 9))
    print("\nChinese Remainder Theorem:")
    print(chinese_remainder_theorem([(2, 3), (3, 5)]))
```

**Expected output:**
```text
Euler Totient Function:
phi(12) = 4

Fermat's Little Theorem:
True

Euler's Theorem:
True

Chinese Remainder Theorem:
(8, 15)
```

---

## 10. Classical Cryptography

### 10.1 Caesar Cipher
The Caesar Cipher is a substitution cipher in which each alphabetic character is shifted by a fixed number of positions.

- **Encryption:** $E(x) = (x + k) \bmod 26$
- **Decryption:** $D(x) = (x - k) \bmod 26$

Where:
- $x$ is the numerical position of a letter.
- $k$ is the shift key.
- $26$ represents the number of English alphabet letters.

**Example:**
```text
Plaintext:  HELLO
Key:        3
Ciphertext: KHOOR
```

### 10.2 Affine Cipher
The Affine Cipher uses a mathematical function to transform each letter.

- **Encryption:** $E(x) = (ax + b) \bmod 26$
- **Decryption:** $D(x) = a^{-1}(x - b) \bmod 26$

The key $a$ must satisfy:
$$\gcd(a, 26) = 1$$
Otherwise, the modular inverse does not exist.

**Example:**
```text
Plaintext: NUMBER
a = 5
b = 8
```
The project implements both encryption and decryption functions.

---

## 11. Public-Key Cryptography: RSA

### 11.1 Introduction
RSA is an asymmetric cryptographic algorithm based on the mathematical properties of prime numbers and modular arithmetic.

It uses two different keys:
- **Public key:** used for encryption.
- **Private key:** used for decryption.

### 11.2 RSA Key Generation
1. **Select two prime numbers:**
   $$p = 61, \quad q = 53$$
2. **Calculate modulus:**
   $$n = pq = 61 \times 53 = 3233$$
3. **Calculate Euler's Totient:**
   $$\varphi(n) = (p - 1)(q - 1) = 60 \times 52 = 3120$$
4. **Select public exponent:**
   Choose $e$ satisfying $1 < e < \varphi(n)$ and $\gcd(e, \varphi(n)) = 1$.
   For example: $e = 17$
5. **Calculate private exponent:**
   Find $d$ such that $ed \equiv 1 \pmod{\varphi(n)}$.
   For the example: $d = 2753$
6. **Construct keys:**
   - **Public key:** $(e, n) = (17, 3233)$
   - **Private key:** $(d, n) = (2753, 3233)$

### 11.3 RSA Encryption
$$C = M^e \bmod n$$
Where $M$ is the integer plaintext and $C$ is the ciphertext.

### 11.4 RSA Decryption
$$M = C^d \bmod n$$
The original message is recovered by applying the private key.

### 11.5 RSA Python Example
```python
# Educational RSA example
p = 61
q = 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17
d = pow(e, -1, phi)

message = 65

# Encryption
ciphertext = pow(message, e, n)

# Decryption
decrypted = pow(ciphertext, d, n)

print("Public key:", (e, n))
print("Private key:", (d, n))
print("Original message:", message)
print("Encrypted message:", ciphertext)
print("Decrypted message:", decrypted)
```

**Expected output:**
```text
Public key: (17, 3233)
Private key: (2753, 3233)
Original message: 65
Encrypted message: 2790
Decrypted message: 65
```

> **Security Warning:** This RSA example is strictly educational. The repository's RSA engine uses small demonstration primes and Python's ordinary random-number generator. It does not implement secure padding or production-grade key management. **Never use this implementation to protect real data.**

---

## 12. Installation and Setup

### Requirements
- Python 3.9 or newer
- Git
- Jupyter Notebook or Google Colab
- Required Python packages

### Clone the repository
```bash
git clone https://github.com/ImSajeeb/NTC-Learning-Laboratory.git
cd NTC-Learning-Laboratory
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run validation
```bash
python validate_repo.py
```

### Generate diagrams
```bash
python generate_diagrams.py
```

### Start Jupyter Notebook
```bash
jupyter notebook
```

---

## 13. Running in Google Colab

Google Colab allows the project to run without installing Python locally. Open [Google Colab](https://colab.research.google.com/), create a new notebook, and execute the following steps:

**Step 1: Clone repository**
```python
!git clone https://github.com/ImSajeeb/NTC-Learning-Laboratory.git
```

**Step 2: Set project directory**
```python
import os
import sys

PROJECT_DIR = "/content/NTC-Learning-Laboratory"
os.chdir(PROJECT_DIR)
sys.path.insert(0, PROJECT_DIR)
print("Project loaded successfully!")
```

**Step 3: Install dependencies**
```python
!pip install -r requirements.txt
```

**Step 4: Run validation**
```python
!python validate_repo.py
```

**Step 5: Explore the theorem module**
```python
import sys
sys.path.insert(0, "/content/NTC-Learning-Laboratory/05_Number_Theory_Theorems")

from theorem_implementations import (
    euler_totient,
    fermat_little_theorem_valid,
    euler_theorem_valid,
    chinese_remainder_theorem
)

print("phi(12):", euler_totient(12))
print("Fermat:", fermat_little_theorem_valid(2, 5))
print("Euler:", euler_theorem_valid(2, 9))
print("CRT:", chinese_remainder_theorem([(2, 3), (3, 5)]))
```

---

## 14. Testing and Verification

The project includes a validation script for checking selected algorithm implementations:

```bash
python validate_repo.py
```

The following mathematical properties should be tested:

| Test | Expected result |
| :--- | :--- |
| `GCD(48, 18)` | `6` |
| `LCM(12, 18)` | `36` |
| `Prime(17)` | `True` |
| `Prime(25)` | `False` |
| `phi(12)` | `4` |
| `Fermat(2, 5)` | `True` |
| `Euler(2, 9)` | `True` |
| `CRT [(2,3), (3,5)]` | `(8, 15)` |
| Caesar encryption/decryption | Original message recovered |
| Affine encryption/decryption | Original message recovered |
| RSA encryption/decryption | Original integer recovered |

The theorem implementation should also be tested with invalid inputs, such as:
- A composite number supplied as the Fermat modulus.
- Non-coprime inputs to Euler's theorem.
- Repeated or non-coprime CRT moduli.
- Zero or negative moduli.

> **Important:** The repository's validation script does not automatically execute every notebook. Notebook execution should be checked separately.

---

## 15. Computational Complexity

| Algorithm | Approximate time complexity |
| :--- | :--- |
| Divisibility checking | $O(1)$ |
| Trial-division primality test | $O(\sqrt{n})$ |
| Prime factorization | $O(\sqrt{n})$ |
| Euclidean Algorithm | $O(\log(\min(a,b)))$ |
| Extended Euclidean Algorithm | $O(\log(\min(a,b)))$ |
| Modular exponentiation | $O(\log \text{exponent})$ modular multiplications |
| Euler Totient Function | $O(\sqrt{n})$ |
| Fermat verification | $O(\log p)$ modular multiplications |
| Euler theorem verification | $O(\log n)$ modular multiplications, excluding totient computation |
| Chinese Remainder Theorem | $O(k^2 + \text{modular arithmetic costs})$ for $k$ pairwise-coprime moduli in this implementation |

*Note: These are algorithmic estimates; actual runtime also depends on the sizes of the integers and the cost of arithmetic operations.*

---

## 16. Applications of Number Theory in Cryptography

Number Theory provides the mathematical foundation for several important cryptographic concepts:

| Mathematical concept | Cryptographic application |
| :--- | :--- |
| Prime numbers | RSA key generation |
| Prime factorization | RSA mathematical security foundation |
| GCD | Checking relatively prime numbers |
| Extended Euclidean Algorithm | Modular inverse calculation |
| Modular arithmetic | Encryption and decryption |
| Euler Totient Function | RSA key construction |
| Fermat's Little Theorem | Modular arithmetic and primality testing |
| Euler's Theorem | RSA correctness and modular exponentiation |
| Chinese Remainder Theorem | Efficient RSA computations |

---

## 17. Educational Limitations and Security Considerations

This project is intended for academic learning and mathematical experimentation. It should not be considered a production cryptography framework.

**Limitations include:**
1. Classical Caesar and Affine ciphers are not secure against modern cryptanalysis.
2. Small RSA primes provide no practical security.
3. Python's standard `random` module is not suitable for cryptographic key generation.
4. RSA requires secure padding and carefully designed protocols for real-world applications.
5. The mathematical verification functions demonstrate selected theorem examples rather than proving theorems in general.
6. Trial-division algorithms become inefficient for very large integers.
7. The Chinese Remainder Theorem implementation in this project requires pairwise-coprime moduli.
8. The existing numbered topic notebooks contain imports that require correction because Python module identifiers cannot begin with digits.

For real cryptographic systems, use established, maintained cryptographic libraries rather than educational implementations.

---

## 18. Learning Outcomes

After completing this project, students should be able to:
- Explain basic concepts of Number Theory.
- Perform prime factorization.
- Calculate GCD and LCM.
- Apply the Euclidean Algorithm.
- Understand Bézout's Identity.
- Solve simple Diophantine equations.
- Perform modular arithmetic.
- Calculate modular inverses.
- Explain Euler's Totient Function.
- State and verify Fermat's Little Theorem.
- State and verify Euler's Theorem.
- Solve modular systems using CRT.
- Understand classical encryption techniques.
- Explain RSA key generation mathematically.
- Implement and test mathematical algorithms using Python.

---

## 19. Future Improvements

Potential future improvements include:
- Add Miller–Rabin primality testing.
- Add a general solver for linear Diophantine equations.
- Support non-coprime systems in a generalized CRT solver.
- Add mathematical visualizations.
- Improve notebook imports and execute all notebooks automatically.
- Add automated unit tests using `pytest`.
- Add interactive theorem demonstrations.
- Improve RSA implementation using secure cryptographic libraries for comparison.
- Add a graphical interface for experimenting with algorithms.

---

## 20. References and Learning Resources

1. Kenneth H. Rosen, *Elementary Number Theory and Its Applications*.
2. Thomas H. Cormen et al., *Introduction to Algorithms*.
3. William Stallings, *Cryptography and Network Security*.
4. Python Documentation: https://docs.python.org/3/
5. SymPy Documentation: https://docs.sympy.org/
6. Jupyter Documentation: https://docs.jupyter.org/
7. Google Colab: https://colab.research.google.com/
8. Original project repository: https://github.com/ImSajeeb/NTC-Learning-Laboratory

---

## 21. Acknowledgement

This project was developed as an academic learning activity to explore Number Theory, computational mathematics, and Cryptography. The project combines mathematical concepts with Python programming to demonstrate the practical relationships between abstract mathematical theories and computer science.

---

## 22. Author

**Md. Sajeeb Khan**
- **Student ID:** IT23032
- **Department:** Information and Communication Technology
- **University:** Mawlana Bhashani Science and Technology University
- **Project:** NTC Learning Laboratory — Number Theory and Cryptography Workshop

---

<p align="center">
  <b>NTC Learning Laboratory</b><br>
  Exploring Number Theory Through Python and Cryptography.
</p>