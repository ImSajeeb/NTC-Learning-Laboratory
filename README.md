# NTC Learning Laboratory
## Number Theory and Cryptography — Class Test (CT) Assignment

<p align="center">
<b>A Python-Based Academic Class Test (CT) Assignment on Number Theory, Mathematical Algorithms, and Cryptography</b>
</p>

<p align="center">
<a href="https://colab.research.google.com/drive/1aSzK7_Pbrc6OdtMI1J6O9Uo00uzeZ0K6?usp=sharing" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
<img src="https://img.shields.io/badge/Python-3.9%2B-blue.svg" alt="Python 3.9+">
<img src="https://img.shields.io/badge/Type-Class%20Test%20(CT)%20Assignment-green.svg" alt="Assignment Type">
<img src="https://img.shields.io/badge/Domain-Number%20Theory-orange.svg" alt="Number Theory">
<img src="https://img.shields.io/badge/Domain-Cryptography-red.svg" alt="Cryptography">
</p>

> **Direct Google Colab Notebook Link:** [Run NTC Learning Laboratory in Google Colab](https://colab.research.google.com/drive/1aSzK7_Pbrc6OdtMI1J6O9Uo00uzeZ0K6?usp=sharing)

---

## 1. Introduction

The **NTC Learning Laboratory** is an academic Class Test (CT) assignment designed to explore the mathematical foundations of Number Theory and their practical applications in Cryptography using Python.

Number Theory is a branch of mathematics that studies integers, prime numbers, divisibility, modular arithmetic, and relationships between numbers. These mathematical concepts form the foundation of many cryptographic algorithms, including RSA.

This repository combines mathematical theory with practical Python implementations. It provides algorithms, Jupyter notebooks, computational experiments, and documentation to demonstrate how mathematical concepts work in real-world computational applications.

The assignment covers seven major areas:
1. Mathematical Foundations
2. Prime Number Analysis
3. GCD and Diophantine Equations
4. Modular Arithmetic
5. Number Theory Theorems
6. Classical Cryptography
7. Public-Key Cryptography (RSA)

The main objective is to connect mathematical definitions, theorem statements, algorithmic implementations, and cryptographic applications.

---

## 2. Assignment Information

| Field | Details |
| :--- | :--- |
| **Repository Name** | NTC Learning Laboratory |
| **Assignment Title** | Number Theory and Cryptography — Class Test (CT) Assignment |
| **Student Name** | Md. Sajeeb Khan |
| **Student ID** | IT23032 |
| **Department** | Information and Communication Technology |
| **University** | Mawlana Bhashani Science and Technology University |
| **Programming Language** | Python |
| **Development Environment** | VS Code, Jupyter Notebook, Google Colab |
| **Google Colab Notebook** | [Open in Google Colab](https://colab.research.google.com/drive/1aSzK7_Pbrc6OdtMI1J6O9Uo00uzeZ0K6?usp=sharing) |
| **Submission Type** | Academic Class Test (CT) Assignment |

---

## 3. Assignment Objectives

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
| **Google Colab** | Cloud-based execution ([Open Notebook](https://colab.research.google.com/drive/1aSzK7_Pbrc6OdtMI1J6O9Uo00uzeZ0K6?usp=sharing)) |
| **Git and GitHub** | Version control and repository hosting |

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
$$6 \mid 48 \quad 	ext{because} \quad 48 = 6 	imes 8$$

However:
$$5 
mid 48$$
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
$$60 = 2^2 	imes 3 	imes 5$$

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
The common divisors are $1, 2, 3, 6$. Therefore, the GCD is $6$.

### 7.2 Euclidean Algorithm
The Euclidean Algorithm calculates the GCD using repeated division.

**Mathematical identity:**
$$\gcd(a, b) = \gcd(b, a mod b)$$

The process continues until the remainder becomes zero.

**Example:**
$$48 = 18 	imes 2 + 12$$
$$18 = 12 	imes 1 + 6$$
$$12 = 6 	imes 2 + 0$$
Therefore, $\gcd(48, 18) = 6$.

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
where $g = \gcd(a, b)$. This identity is known as **Bézout's Identity**.

**Example:**
For $a = 30$ and $b = 12$:
$$30(1) + 12(-2) = 6$$
Therefore: $x = 1, y = -2, g = 6$.

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
$$\operatorname{lcm}(a, b) = rac{|a 	imes b|}{\gcd(a, b)}$$

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
Since $\gcd(6, 9) = 3$ and $3 \mid 3$, integer solutions exist. One solution is $x = 2, y = -1$ because $6(2) + 9(-1) = 3$.

---

## 8. Modular Arithmetic

### 8.1 Modular Congruence
Two integers $a$ and $b$ are congruent modulo $m$ if their difference is divisible by $m$:
$$a \equiv b \pmod{m}$$
Equivalent condition: $m \mid (a - b)$.

**Example:** $17 \equiv 5 \pmod{12}$ because $17 - 5 = 12$.

### 8.2 Modular Addition
$$(a + b) mod m$$
Example: $(7 + 5) mod 11 = 1$

```python
def mod_add(a, b, m):
    if m <= 0:
        raise ValueError("Modulus must be positive.")
    return (a + b) % m

print(mod_add(7, 5, 11))
```

### 8.3 Modular Subtraction
$$(a - b) mod m$$
Example: $(7 - 5) mod 11 = 2$

```python
def mod_sub(a, b, m):
    if m <= 0:
        raise ValueError("Modulus must be positive.")
    return (a - b) % m

print(mod_sub(7, 5, 11))
```

### 8.4 Modular Multiplication
$$(a 	imes b) mod m$$
Example: $(7 	imes 5) mod 11 = 2$

```python
def mod_mul(a, b, m):
    if m <= 0:
        raise ValueError("Modulus must be positive.")
    return (a * b) % m

print(mod_mul(7, 5, 11))
```

### 8.5 Modular Exponentiation
$$a^b mod m$$
Example: $2^{10} mod 13 = 10$

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
The inverse exists if and only if $\gcd(a, m) = 1$.

**Example:** $3 	imes 4 = 12$, and $12 mod 11 = 1$. Therefore, $3^{-1} \equiv 4 \pmod{11}$.

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

This section demonstrates how core number theory theorems are translated into Python algorithms and computationally verified:
1. Euler's Totient Function
2. Fermat's Little Theorem
3. Euler's Theorem
4. Chinese Remainder Theorem

### 9.1 Euler's Totient Function

**Definition:**  
Euler's Totient Function, represented by $arphi(n)$, counts the number of positive integers less than or equal to $n$ that are relatively prime to $n$:
$$arphi(n) = |\{k : 1 \le k \le n, \gcd(k, n) = 1\}|$$

**Formula:**  
If the distinct prime factors of $n$ are $p_1, p_2, \dots, p_k$, then:
$$arphi(n) = n \prod_{p \mid n} \left(1 - rac{1}{p}ight)$$

**Example: Calculate $arphi(12)$**  
Prime factorization: $12 = 2^2 	imes 3$
$$arphi(12) = 12\left(1 - rac{1}{2}ight)\left(1 - rac{1}{3}ight) = 12 	imes rac{1}{2} 	imes rac{2}{3} = 4$$
The positive integers from $1$ to $12$ relatively prime to $12$ are $1, 5, 7, 11$.

**Python implementation:**
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

- **Applications:** RSA public-key cryptography, calculating the size of the multiplicative group modulo $n$, Euler's theorem, and modular multiplicative inverses.
- **Time Complexity:** Approximately $O(\sqrt{n})$ divisor checks in the worst case using trial division.

### 9.2 Fermat's Little Theorem

**Statement:**  
If $p$ is a prime number and $a$ is an integer relatively prime to $p$ ($\gcd(a, p) = 1$), then:
$$a^{p-1} \equiv 1 \pmod{p}$$

**Example:**  
Let $a = 2, p = 5$:
$$2^{5-1} = 2^4 = 16 \equiv 1 \pmod{5}$$

**Python implementation:**
```python
from math import gcd

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

- **Applications:** Prime number testing, modular arithmetic, RSA foundations, and modular inverse calculations.
- **Important Note:** Passing a single Fermat test provides a necessary property for primes, but composite numbers (such as Carmichael numbers) can sometimes pass Fermat tests.

### 9.3 Euler's Theorem

**Statement:**  
Euler's theorem generalizes Fermat's Little Theorem. If $a$ and $n$ are relatively prime ($\gcd(a, n) = 1$), then:
$$a^{arphi(n)} \equiv 1 \pmod{n}$$

**Example:**  
Let $a = 2, n = 9$. First, $arphi(9) = 9\left(1 - rac{1}{3}ight) = 6$.
$$2^6 = 64 \equiv 1 \pmod{9}$$

**Python implementation:**
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

- **Applications:** RSA encryption/decryption correctness, modular exponentiation reduction, and cryptographic key construction.

### 9.4 Chinese Remainder Theorem (CRT)

**Statement:**  
If the moduli $m_1, m_2, \dots, m_k$ are pairwise relatively prime, then the system of congruences:
$$x \equiv a_1 \pmod{m_1}$$
$$x \equiv a_2 \pmod{m_2}$$
$$dots$$
$$x \equiv a_k \pmod{m_k}$$
has a unique solution modulo $M = m_1 m_2 \cdots m_k$.

**Example:**  
Solve $x \equiv 2 \pmod{3}$ and $x \equiv 3 \pmod{5}$.
1. $M = 3 	imes 5 = 15$
2. $M_1 = rac{15}{3} = 5$, $M_2 = rac{15}{5} = 3$
3. Modular inverses: $5^{-1} \equiv 2 \pmod{3}$ and $3^{-1} \equiv 2 \pmod{5}$
4. Apply formula:
$$x = \sum_{i=1}^k a_i M_i y_i \pmod{M}$$
$$x = (2 	imes 5 	imes 2) + (3 	imes 3 	imes 2) = 20 + 18 = 38 \equiv 8 \pmod{15}$$

**Verification:** $8 mod 3 = 2$ and $8 mod 5 = 3$.

**Python implementation:**
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

solution, combined_modulus = chinese_remainder_theorem([(2, 3), (3, 5)])
print("Solution:", solution)
print("Combined modulus:", combined_modulus)
```

**Output:**
```text
Solution: 8
Combined modulus: 15
```

### 9.5 Complete Number Theory Theorem Implementation
File: `05_Number_Theory_Theorems/theorem_implementations.py`

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
Each alphabetic character is shifted by a fixed number of positions $k$:
- **Encryption:** $E(x) = (x + k) mod 26$
- **Decryption:** $D(x) = (x - k) mod 26$

```text
Plaintext:  HELLO
Key:        3
Ciphertext: KHOOR
```

### 10.2 Affine Cipher
Uses a linear modular function to transform each letter:
- **Encryption:** $E(x) = (ax + b) mod 26$
- **Decryption:** $D(x) = a^{-1}(x - b) mod 26$

The key $a$ must satisfy $\gcd(a, 26) = 1$ so that $a^{-1}$ exists.

```text
Plaintext: NUMBER
a = 5, b = 8
```

---

## 11. Public-Key Cryptography: RSA

### 11.1 Introduction
RSA is an asymmetric cryptographic algorithm based on prime factorization and modular arithmetic, utilizing a **Public Key** $(e, n)$ for encryption and a **Private Key** $(d, n)$ for decryption.

### 11.2 RSA Key Generation
1. **Select two prime numbers:** $p = 61, q = 53$
2. **Calculate modulus:** $n = pq = 61 	imes 53 = 3233$
3. **Calculate Euler's Totient:** $arphi(n) = (p - 1)(q - 1) = 60 	imes 52 = 3120$
4. **Select public exponent:** Choose $e$ such that $1 < e < arphi(n)$ and $\gcd(e, arphi(n)) = 1$ (e.g., $e = 17$)
5. **Calculate private exponent:** Find $d$ such that $ed \equiv 1 \pmod{arphi(n)}$ ($d = 2753$)
6. **Construct keys:** Public key $= (17, 3233)$, Private key $= (2753, 3233)$

### 11.3 Encryption & Decryption Formulas
- **Encryption:** $C = M^e mod n$
- **Decryption:** $M = C^d mod n$

### 11.4 RSA Python Example
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

> **Security Warning:** This RSA example is strictly educational for coursework demonstration. It uses small demonstration primes and Python's non-cryptographic random generator without secure padding.

---

## 12. Installation and Setup

### Requirements
- Python 3.9 or newer
- Git
- Jupyter Notebook or Google Colab

### Local Execution
```bash
# Clone the repository
git clone https://github.com/ImSajeeb/NTC-Learning-Laboratory.git
cd NTC-Learning-Laboratory

# Install dependencies
pip install -r requirements.txt

# Run validation
python validate_repo.py

# Generate diagrams
python generate_diagrams.py

# Start Jupyter Notebook
jupyter notebook
```

---

## 13. Running in Google Colab

You can run the complete assignment directly in the cloud using the official notebook:  
**[Open NTC Learning Laboratory in Google Colab](https://colab.research.google.com/drive/1aSzK7_Pbrc6OdtMI1J6O9Uo00uzeZ0K6?usp=sharing)**

Or run the setup manually in any Colab environment:

**Step 1: Clone repository**
```python
!git clone https://github.com/ImSajeeb/NTC-Learning-Laboratory.git
```

**Step 2: Set working directory**
```python
import os
import sys

PROJECT_DIR = "/content/NTC-Learning-Laboratory"
os.chdir(PROJECT_DIR)
sys.path.insert(0, PROJECT_DIR)
print("Workspace loaded successfully!")
```

**Step 3: Install dependencies & validate**
```python
!pip install -r requirements.txt
!python validate_repo.py
```

**Step 4: Explore the theorem module**
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

Run `python validate_repo.py` to verify the core implementations:

| Test | Expected Result |
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

The theorem module is also tested against invalid inputs (e.g., composite Fermat moduli, non-coprime Euler inputs, non-coprime CRT moduli, and non-positive moduli).

---

## 15. Computational Complexity

| Algorithm | Approximate Time Complexity |
| :--- | :--- |
| Divisibility checking | $O(1)$ |
| Trial-division primality test | $O(\sqrt{n})$ |
| Prime factorization | $O(\sqrt{n})$ |
| Euclidean Algorithm | $O(\log(\min(a, b)))$ |
| Extended Euclidean Algorithm | $O(\log(\min(a, b)))$ |
| Modular exponentiation | $O(\log 	ext{exponent})$ modular multiplications |
| Euler Totient Function | $O(\sqrt{n})$ |
| Fermat verification | $O(\log p)$ modular multiplications |
| Euler theorem verification | $O(\log n)$ modular multiplications (excluding totient) |
| Chinese Remainder Theorem | $O(k^2 + 	ext{modular arithmetic costs})$ for $k$ moduli |

---

## 16. Applications of Number Theory in Cryptography

| Mathematical Concept | Cryptographic Application |
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

1. Classical Caesar and Affine ciphers are vulnerable to frequency analysis and brute-force attacks.
2. Small RSA primes provide no practical cryptographic security.
3. Python's standard `random` module is not cryptographically secure.
4. Real-world RSA requires secure padding schemes (such as OAEP).
5. Verification functions test concrete examples rather than serving as formal mathematical proofs.
6. Trial-division algorithms become inefficient for large integers.
7. The CRT solver requires pairwise-coprime moduli.
8. Numbered topic folders require `sys.path` or `importlib` loading because Python module identifiers cannot start with digits.

---

## 18. Learning Outcomes

- Explain fundamental concepts of Number Theory and divisibility.
- Perform prime factorization and primality testing.
- Apply the Euclidean and Extended Euclidean Algorithms (Bézout's Identity).
- Solve linear Diophantine equations and modular systems using CRT.
- State and verify Euler's Totient Function, Fermat's Little Theorem, and Euler's Theorem.
- Implement classical ciphers (Caesar, Affine) and asymmetric RSA encryption in Python.

---

## 19. Future Improvements

- Add Miller–Rabin probabilistic primality testing.
- Implement a general solver for linear Diophantine equations.
- Extend CRT to handle non-coprime moduli systems.
- Add automated unit tests with `pytest`.
- Add interactive visualizations for modular arithmetic and prime distributions.

---

## 20. References and Learning Resources

1. Kenneth H. Rosen, *Elementary Number Theory and Its Applications*.
2. Thomas H. Cormen et al., *Introduction to Algorithms*.
3. William Stallings, *Cryptography and Network Security*.
4. Python Documentation: https://docs.python.org/3/
5. SymPy Documentation: https://docs.sympy.org/
6. Google Colab Notebook: https://colab.research.google.com/drive/1aSzK7_Pbrc6OdtMI1J6O9Uo00uzeZ0K6?usp=sharing
7. GitHub Repository: https://github.com/ImSajeeb/NTC-Learning-Laboratory

---

## 21. Acknowledgement

This work was developed as an academic **Class Test (CT) Assignment** to explore Number Theory, computational mathematics, and Cryptography, demonstrating the practical bridge between abstract mathematical theorems and Python programming.

---

## 22. Author

**Md. Sajeeb Khan**  
- **Student ID:** IT23032  
- **Department:** Information and Communication Technology  
- **University:** Mawlana Bhashani Science and Technology University  
- **Assignment:** NTC Learning Laboratory — Number Theory and Cryptography Class Test (CT) Assignment  

<p align="center">
<b>NTC Learning Laboratory</b><br>
Exploring Number Theory Through Python and Cryptography.
</p>
