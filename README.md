# Number Theory and Cryptography
**Name:** Md. Sajeeb Khan
**Student ID:** IT23032
**Department:** Information and Communication Technology (ICT)
**University:** Mawlana Bhashani Science and Technology University (MBSTU)

**Project:** NTC Learning Laboratory

## 1. Introduction
This project was developed as a compact academic learning repository for the workshop on Number Theory and Cryptography. The goal is to connect mathematical foundations with practical Python implementations and a few carefully chosen computational checks. The emphasis is on correctness, clarity, and acceptable university-level academic quality rather than unnecessary complexity.

## 2. Objectives
- Study the core topics from the official workshop reference.
- Understand the mathematical reasoning behind each algorithm.
- Implement the important techniques in Python.
- Validate the results with worked examples.
- Prepare a readable GitHub repository for assignment submission and viva preparation.

## 3. Reference Repository
Official reference: https://github.com/mnp-club/Number_Theory_and_Cryptography_Workshop

The project follows the workshop’s learning path: integer arithmetic, divisibility, prime numbers, GCD/LCM, modular arithmetic, number theory theorems, and public-key cryptography with RSA.

## 4. Topics Covered
- Divisibility and prime numbers
- Prime factorization
- GCD and Euclidean algorithm
- Extended Euclidean algorithm
- LCM
- Modular arithmetic and congruence
- Modular inverse
- Euler’s totient function
- Fermat’s little theorem
- Euler’s theorem
- Chinese remainder theorem
- Classical cryptography foundations
- RSA fundamentals

## 5. Repository Structure
```text
NTC-Learning-Laboratory/
├── README.md
├── requirements.txt
├── .gitignore
├── notebooks/
│   ├── 01_Number_Theory.ipynb
│   ├── 02_Modular_Arithmetic.ipynb
│   ├── 03_Number_Theory_Algorithms.ipynb
│   ├── 04_Cryptography.ipynb
│   └── 05_RSA_Implementation.ipynb
├── src/
│   ├── number_theory.py
│   ├── modular_arithmetic.py
│   └── cryptography.py
├── figures/
├── documentation/
│   └── viva_questions.md
└── existing workshop files retained for validation
```

## 6. Mathematical Foundation
Important formulas used in the project:

- Divisibility: $a \mid b$ means $b = ak$ for some integer $k$.
- GCD recurrence: $\gcd(a, b) = \gcd(b, a \bmod b)$.
- LCM formula: $\operatorname{lcm}(a, b) = \frac{|a \times b|}{\gcd(a, b)}$.
- Congruence: $a \equiv b \pmod m$ means $m \mid (a-b)$.
- Euler totient: $\varphi(n) = n \prod_{p\mid n} \left(1 - \frac{1}{p}\right)$.
- RSA encryption: $c \equiv m^e \pmod n$.
- RSA decryption: $m \equiv c^d \pmod n$.

## 7. Implementation Summary
The project contains Python implementations for:
- prime testing and factorization,
- GCD and LCM,
- extended Euclidean algorithm,
- modular addition, subtraction, multiplication, and exponentiation,
- modular inverse,
- Euler’s theorem checks,
- classical cipher examples,
- RSA key generation and encryption/decryption.

## 8. Installation
```bash
cd NTC-Learning-Laboratory
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
# source .venv/bin/activate
pip install -r requirements.txt
```

## 9. Running the Project
```bash
cd NTC-Learning-Laboratory
jupyter notebook notebooks
```
Open the notebook files and run the code cells in order.

## 10. Google Colab
1. Open https://colab.research.google.com/
2. Upload a notebook from the `notebooks/` folder.
3. Run the code cells sequentially.
4. Install dependencies if required.

## 11. Results and Learning Outcomes
The implemented examples validate the key ideas, including:
- $\gcd(48,18)=6$
- $\operatorname{lcm}(12,18)=36$
- $7 + 5 \equiv 1 \pmod{11}$
- inverse of 3 modulo 11 is 4
- RSA encryption/decryption recovers the original integer for a small educational example

This work demonstrates how mathematical theory becomes executable algorithmic logic and how those ideas support cryptographic systems.

## 12. Conclusion
This repository is a compact, practical, and academically meaningful assignment submission. It prioritizes conceptual correctness, algorithmic implementation, and clear educational presentation over unnecessary complexity.

## 13. References
- https://github.com/mnp-club/Number_Theory_and_Cryptography_Workshop
- Course notes and workshop material on modular arithmetic, number theory, and cryptography
