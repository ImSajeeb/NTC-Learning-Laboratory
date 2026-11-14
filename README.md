# Number Theory and Cryptography Workshop

This academic project explores how number theory provides mathematical tools for cryptography. It combines Python implementations of core algorithms with topic notebooks, computational experiments, and written study material. The examples are intended to support learning and demonstration.

## Student Information

| Field | Details |
|---|---|
| Name | Md. Sajeeb Khan |
| Student ID | IT23032 |
| Department | Information and Communication Technology (ICT) |
| University | Mawlana Bhashani Science and Technology University (MBSTU) |
| Project | Number Theory and Cryptography Workshop |

## Project Overview

The workshop follows a path from integer arithmetic and prime numbers to modular arithmetic and cryptographic examples. Python implementations make selected algorithms concrete, while the notebooks and experiments provide worked examples and computational observations. The project is for university-level study and is not a production cryptography library.

The project uses the [Number Theory and Cryptography Workshop repository](https://github.com/mnp-club/Number_Theory_and_Cryptography_Workshop) as its learning reference. This project is an independent academic work and is not affiliated with or endorsed by that repository.

## Learning Objectives

- Explain divisibility, prime factorization, GCD, LCM, and modular congruence.
- Trace the Euclidean and extended Euclidean algorithms.
- Implement number-theoretic and modular arithmetic operations in Python.
- Use computation to check examples and observe prime and totient values.
- Relate modular arithmetic and prime numbers to classical ciphers and RSA.
- Recognize the limits of small, textbook cryptography examples.

## Topics Covered

1. **Mathematical foundations:** divisibility, positive divisors, and integer arithmetic.
2. **Prime number analysis and factorization:** primality testing, prime enumeration, and trial-division factorization.
3. **GCD, LCM, and Euclidean algorithms:** Euclidean GCD, extended GCD, and LCM.
4. **Modular arithmetic and congruences:** modular addition, subtraction, multiplication, exponentiation, and inverses.
5. **Number theory theorems:** Euler's totient function, Fermat's Little Theorem, Euler's theorem, and the Chinese Remainder Theorem (CRT).
6. **Classical cryptography:** Caesar and Affine ciphers.
7. **Public-key cryptography and RSA:** educational RSA key generation and integer encryption/decryption.

## Repository Structure

```text
.
├── .gitignore
├── README.md
├── requirements.txt
├── validate_repo.py
├── debug_validate.py
├── generate_diagrams.py
├── 01_Mathematical_Foundations/
│   ├── __init__.py
│   ├── arithmetic_operations.py
│   └── mathematical_concepts.ipynb
├── 02_Prime_Number_Analysis/
│   ├── __init__.py
│   ├── prime_tools.py
│   └── prime_number_exploration.ipynb
├── 03_GCD_and_Diophantine_Equations/
│   ├── __init__.py
│   ├── euclidean_methods.py
│   └── gcd_experiments.ipynb
├── 04_Modular_Systems/
│   ├── __init__.py
│   ├── modular_operations.py
│   └── modular_arithmetic.ipynb
├── 05_Number_Theory_Theorems/
│   ├── __init__.py
│   ├── theorem_implementations.py
│   └── fermat_euler_crt.ipynb
├── 06_Cryptographic_Methods/
│   ├── __init__.py
│   ├── classical_ciphers.py
│   └── cryptography_fundamentals.ipynb
├── 07_Public_Key_Cryptography/
│   ├── __init__.py
│   ├── rsa_engine.py
│   └── rsa_algorithm_explained.ipynb
├── documentation/
│   ├── mathematical_notes.md
│   ├── references.md
│   ├── viva_preparation.md
│   └── viva_questions.md
├── experiments/
│   ├── algorithm_verification.ipynb
│   └── computational_observations.ipynb
├── figures/
│   └── .gitkeep
├── notebooks/
│   ├── 01_Number_Theory.ipynb
│   ├── 02_Modular_Arithmetic.ipynb
│   ├── 03_Number_Theory_Algorithms.ipynb
│   ├── 04_Cryptography.ipynb
│   └── 05_RSA_Implementation.ipynb
└── src/
    ├── __init__.py
    ├── cryptography.py
    ├── modular_arithmetic.py
    └── number_theory.py
```

`generate_diagrams.py` writes generated PNG files to `assets/diagrams/`; that output directory is created when the script runs and is not part of the current tracked tree.

## Mathematical Foundations

Let \(a,b,k\) be integers and let \(m\) be a positive modulus.

- **Divisibility:** \(a\mid b\) means that \(b=ak\) for some integer \(k\).
- **Prime factorization:** Every integer \(n>1\) can be expressed uniquely, up to ordering, as a product of primes:
  \[
  n = \prod_{i=1}^{r} p_i^{e_i}.
  \]
- **Greatest common divisor:** The Euclidean recurrence is
  \[
  \gcd(a,b)=\gcd(b,\,a\bmod b),
  \]
  iterated until the remainder is zero.
- **Least common multiple:** For nonzero \(a,b\),
  \[
  \operatorname{lcm}(a,b)=\frac{|ab|}{\gcd(a,b)}.
  \]
  The implementation defines the LCM as \(0\) when either input is zero.
- **Modular congruence:** \(a\equiv b\pmod m\) exactly when \(m\mid(a-b)\).
- **Modular inverse:** \(x\) is the inverse of \(a\) modulo \(m\) if
  \[
  ax\equiv 1\pmod m.
  \]
  Such an inverse exists exactly when \(\gcd(a,m)=1\).
- **Euler's totient function:** \(\varphi(n)\) counts the integers from \(1\) through \(n\) that are relatively prime to \(n\). Using the distinct prime divisors \(p\) of \(n\),
  \[
  \varphi(n)=n\prod_{p\mid n}\left(1-\frac{1}{p}\right).
  \]
- **Fermat's Little Theorem:** If \(p\) is prime and \(p\nmid a\), then
  \[
  a^{p-1}\equiv 1\pmod p.
  \]
- **Euler's theorem:** If \(\gcd(a,n)=1\), then
  \[
  a^{\varphi(n)}\equiv 1\pmod n.
  \]
- **Chinese Remainder Theorem:** For pairwise coprime moduli \(m_1,\ldots,m_r\), a system
  \[
  x\equiv a_i\pmod{m_i}\quad(1\le i\le r)
  \]
  has a unique solution modulo \(M=\prod_{i=1}^{r}m_i\).

## Algorithms and Implementations

The numbered topic folders contain the chapter implementations; `src/` provides a second set of reusable implementations used by the five guided notebooks.

| Module | Implemented operations |
|---|---|
| [`01_Mathematical_Foundations/arithmetic_operations.py`](01_Mathematical_Foundations/arithmetic_operations.py) | `is_divisible`, `positive_divisors`, `prime_factorization`, `factor_count`, and `sum_of_divisors` |
| [`02_Prime_Number_Analysis/prime_tools.py`](02_Prime_Number_Analysis/prime_tools.py) | `is_prime`, `primes_up_to`, and `prime_factorization`; primality and factorization use trial division |
| [`03_GCD_and_Diophantine_Equations/euclidean_methods.py`](03_GCD_and_Diophantine_Equations/euclidean_methods.py) | `gcd`, `extended_gcd` (returns \(g,x,y\) with \(ax+by=g\)), and `lcm` |
| [`04_Modular_Systems/modular_operations.py`](04_Modular_Systems/modular_operations.py) | `mod_add`, `mod_sub`, `mod_mul`, `mod_pow`, and `mod_inverse`; modular exponentiation uses repeated squaring and the inverse uses extended GCD |
| [`05_Number_Theory_Theorems/theorem_implementations.py`](05_Number_Theory_Theorems/theorem_implementations.py) | `euler_totient`, `fermat_little_theorem_valid`, `euler_theorem_valid`, and `chinese_remainder_theorem` |
| [`06_Cryptographic_Methods/classical_ciphers.py`](06_Cryptographic_Methods/classical_ciphers.py) | `caesar_encrypt`, `caesar_decrypt`, `affine_encrypt`, and `affine_decrypt` |
| [`07_Public_Key_Cryptography/rsa_engine.py`](07_Public_Key_Cryptography/rsa_engine.py) | `generate_prime`, `generate_rsa_keypair`, `rsa_encrypt`, `rsa_decrypt`, and `string_to_int` |
| [`src/number_theory.py`](src/number_theory.py), [`src/modular_arithmetic.py`](src/modular_arithmetic.py), [`src/cryptography.py`](src/cryptography.py) | Reusable counterparts for number theory, modular operations, Caesar/Affine ciphers, and RSA |

The RSA functions operate on integer messages \(0\le m<n\). The `string_to_int` helpers convert text to an integer, but the project does not provide a complete text-encryption format or protocol.

## Jupyter Notebook Guide

The notebook descriptions below are based on their titles, explanatory text, imports, and code cells.

| Notebook | Main subject | What a student studies |
|---|---|---|
| [`01_Mathematical_Foundations/mathematical_concepts.ipynb`](01_Mathematical_Foundations/mathematical_concepts.ipynb) | Divisibility and arithmetic | Divisibility checks, positive divisors, and prime factorization |
| [`02_Prime_Number_Analysis/prime_number_exploration.ipynb`](02_Prime_Number_Analysis/prime_number_exploration.ipynb) | Prime analysis | Primality tests, listing primes, and factorization |
| [`03_GCD_and_Diophantine_Equations/gcd_experiments.ipynb`](03_GCD_and_Diophantine_Equations/gcd_experiments.ipynb) | GCD and Diophantine methods | Euclidean GCD, extended GCD, and LCM |
| [`04_Modular_Systems/modular_arithmetic.ipynb`](04_Modular_Systems/modular_arithmetic.ipynb) | Modular systems | Modular operations, exponentiation, and inverses |
| [`05_Number_Theory_Theorems/fermat_euler_crt.ipynb`](05_Number_Theory_Theorems/fermat_euler_crt.ipynb) | Number theory theorems | Totient values, Fermat checks, and a CRT example |
| [`06_Cryptographic_Methods/cryptography_fundamentals.ipynb`](06_Cryptographic_Methods/cryptography_fundamentals.ipynb) | Classical ciphers | Caesar and Affine encryption/decryption examples |
| [`07_Public_Key_Cryptography/rsa_algorithm_explained.ipynb`](07_Public_Key_Cryptography/rsa_algorithm_explained.ipynb) | RSA theory and practice | Small RSA key generation and integer round-trip example |
| [`experiments/algorithm_verification.ipynb`](experiments/algorithm_verification.ipynb) | Algorithm checks | Assertions for GCD, LCM, primality, and modular inverse |
| [`experiments/computational_observations.ipynb`](experiments/computational_observations.ipynb) | Computational observations | Prime lists and Euler totient values for selected integers |
| [`notebooks/01_Number_Theory.ipynb`](notebooks/01_Number_Theory.ipynb) | Number theory fundamentals | Divisibility, primes, factorization, GCD, and LCM |
| [`notebooks/02_Modular_Arithmetic.ipynb`](notebooks/02_Modular_Arithmetic.ipynb) | Modular arithmetic | Congruences, modular operations, and inverses |
| [`notebooks/03_Number_Theory_Algorithms.ipynb`](notebooks/03_Number_Theory_Algorithms.ipynb) | Number theory algorithms | Euclidean methods, totient, and CRT |
| [`notebooks/04_Cryptography.ipynb`](notebooks/04_Cryptography.ipynb) | Classical cryptography | Caesar and Affine cipher examples and practice questions |
| [`notebooks/05_RSA_Implementation.ipynb`](notebooks/05_RSA_Implementation.ipynb) | RSA implementation | Educational integer RSA key generation, encryption, and decryption |

**Notebook import note:** the seven notebooks in the numbered topic folders and the two in `experiments/` currently contain Python imports such as `from 01_Mathematical_Foundations...`. Since Python identifiers cannot begin with digits, these code cells have syntax errors as written. The five notebooks in `notebooks/` import from `src/` and expect the repository root (or its parent) on the Python path. The validation script below does not execute notebooks.

## Installation and Setup

Install Python before following these steps. In Windows PowerShell, clone the repository, create a virtual environment, activate it, and install the listed dependencies:

```powershell
git clone https://github.com/ImSajeeb/NTC-Learning-Laboratory.git
cd NTC-Learning-Laboratory

python -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

The requirements include NumPy, Matplotlib, Jupyter, and Notebook. NumPy and Matplotlib are used by [`generate_diagrams.py`](generate_diagrams.py).

## Running the Project

From the repository root, launch Jupyter:

```powershell
jupyter notebook
```

In Visual Studio Code:

1. Open the cloned project folder.
2. Install the Python and Jupyter extensions if they are not already installed.
3. Select the Python interpreter and notebook kernel from the project's `.venv`.
4. Open a notebook.
5. Run its cells in order. See the notebook import note above for current limitations in the chapter and experiment notebooks.

## Google Colab

You can upload an individual `.ipynb` file to Google Colab and run its cells there when its imports and dependencies are available. The five notebooks under `notebooks/` import project code from `src/`, so uploading only the notebook is not sufficient; upload the required `src/` files as well or clone the repository in the Colab runtime and use the repository root as the working directory. The numbered-topic and experiment notebooks also need their import statements corrected before their code cells can run in Colab.

## Experiments and Validation

[`experiments/algorithm_verification.ipynb`](experiments/algorithm_verification.ipynb) contains assertions for selected algorithms, and [`experiments/computational_observations.ipynb`](experiments/computational_observations.ipynb) prints prime and totient examples. Their current import syntax prevents their code cells from executing as written.

[`validate_repo.py`](validate_repo.py) is the executable core validation script. It loads the seven topic modules and checks representative divisibility, divisor/factorization, prime, GCD/extended-GCD/LCM, modular arithmetic/inverse, totient, theorem, Caesar/Affine cipher, RSA round-trip, and CRT results. **Confirmed:** running `python validate_repo.py` in this repository printed `All core validation checks passed.` This script validates selected Python functions; it does not run or validate notebook cells. [`debug_validate.py`](debug_validate.py) is a diagnostic script that loads modules and prints sample results.

## Educational Limitations

- The RSA implementation is for education and demonstration only, not production security.
- Its demonstration primes and keys are small and insecure; its key generation uses Python's `random` module.
- Real-world RSA requires secure key generation, appropriate padding schemes, and vetted cryptographic libraries. This project implements neither production-grade padding nor a secure protocol.
- Caesar and Affine ciphers are classical examples and are not secure against modern attacks.
- The notebook import issues described above have not been repaired in this documentation-only update.

## Viva Preparation

- [Viva preparation notes](documentation/viva_preparation.md)
- [Viva preparation questions](documentation/viva_questions.md)

## Learning Outcomes

The project brings together mathematical definitions and working Python examples: tracing Euclidean algorithms, computing primes and modular inverses, applying number theory theorems, solving a CRT example, and observing how modular arithmetic is used in classical ciphers and an educational RSA demonstration. The validation script provides a reproducible check of selected core functions.

## References and Acknowledgements

- [Number Theory and Cryptography Workshop](https://github.com/mnp-club/Number_Theory_and_Cryptography_Workshop) — the project's stated learning reference; no affiliation or endorsement is implied.
- [Mathematical notes](documentation/mathematical_notes.md) — definitions, theorem statements, and a small RSA example.
- [References and resource notes](documentation/references.md) — records the workshop repository as the external reference used by the project.

## Author

| Field | Details |
|---|---|
| Name | Md. Sajeeb Khan |
| Student ID | IT23032 |
| Department | Information and Communication Technology (ICT) |
| University | Mawlana Bhashani Science and Technology University (MBSTU) |
| Project | Number Theory and Cryptography Workshop |
