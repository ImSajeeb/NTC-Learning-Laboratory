# Number Theory and Cryptography Learning Laboratory

An educational Python project exploring the number-theory concepts behind modern cryptography. It combines chapter-based implementations, Jupyter notebooks, worked examples, and small validation checks.

- **Author:** Md. Sajeeb Khan
- **Student ID:** IT23032
- **Department:** Information and Communication Technology (ICT)
- **University:** Mawlana Bhashani Science and Technology University (MBSTU)

## Learning topics

- Divisibility, prime numbers, and prime factorization
- Euclidean and extended Euclidean algorithms; GCD and LCM
- Modular arithmetic, modular inverses, and congruences
- Euler's totient function, Fermat's little theorem, and Euler's theorem
- Chinese remainder theorem
- Caesar and affine ciphers
- RSA key generation and integer encryption/decryption

## Repository layout

```text
.
├── 01_Mathematical_Foundations/       # Divisibility and arithmetic
├── 02_Prime_Number_Analysis/          # Primes and factorization
├── 03_GCD_and_Diophantine_Equations/  # Euclidean methods
├── 04_Modular_Systems/                # Modular operations
├── 05_Number_Theory_Theorems/         # Fermat, Euler, and CRT
├── 06_Cryptographic_Methods/          # Classical ciphers
├── 07_Public_Key_Cryptography/        # RSA
├── documentation/                     # Mathematical notes and viva material
├── experiments/                       # Computational investigations
├── figures/                           # Project figures
├── notebooks/                         # Guided topic notebooks
├── src/                               # Reusable Python implementations
├── requirements.txt
├── validate_repo.py                   # Core validation checks
└── generate_diagrams.py               # Diagram-generation utility
```

The numbered directories present the material as a learning sequence. The `notebooks/` directory contains guided notebooks, while `src/` provides reusable implementations of number theory, modular arithmetic, and cryptography.

## Setup

Python 3.8 or newer is recommended. From the repository root, create and activate a virtual environment, then install the project dependencies:

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run and validate

Launch Jupyter from the repository root:

```bash
python -m jupyter notebook
```

Open a notebook in `notebooks/` or in one of the numbered topic directories, and run its cells in order. To run the repository's core checks:

```bash
python validate_repo.py
```

A successful validation prints `All core validation checks passed.` The checks cover representative arithmetic, number theory, modular arithmetic, cipher, RSA, and CRT examples.

## Educational use

The implementations and examples are intended for learning and demonstration, not production security. In particular, the classical ciphers and small, textbook-style RSA implementation are not suitable for protecting real data.

## Reference

The project follows topics from the [Number Theory and Cryptography Workshop](https://github.com/mnp-club/Number_Theory_and_Cryptography_Workshop).
