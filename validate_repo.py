import importlib.util
import sys
from pathlib import Path

root = Path(__file__).resolve().parent


def load_module(name: str, file_path: Path):
    spec = importlib.util.spec_from_file_location(name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f'Could not load module from {file_path}')
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


ar = load_module('arith', root / '01_Mathematical_Foundations' / 'arithmetic_operations.py')
pt = load_module('pt', root / '02_Prime_Number_Analysis' / 'prime_tools.py')
gcdm = load_module('gcdm', root / '03_GCD_and_Diophantine_Equations' / 'euclidean_methods.py')
modm = load_module('modm', root / '04_Modular_Systems' / 'modular_operations.py')
thm = load_module('thm', root / '05_Number_Theory_Theorems' / 'theorem_implementations.py')
cipher = load_module('cipher', root / '06_Cryptographic_Methods' / 'classical_ciphers.py')
rsa = load_module('rsa', root / '07_Public_Key_Cryptography' / 'rsa_engine.py')

assert ar.is_divisible(48, 6) is True
assert ar.positive_divisors(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36]
assert ar.prime_factorization(60) == [2, 2, 3, 5]
assert pt.is_prime(17) is True and pt.is_prime(25) is False
assert pt.primes_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
assert gcdm.gcd(48, 18) == 6 and gcdm.gcd(0, 12) == 12
assert gcdm.extended_gcd(30, 12)[0] == 6
assert gcdm.lcm(12, 18) == 36 and gcdm.lcm(0, 12) == 0
assert modm.mod_add(7, 5, 11) == 1
assert modm.mod_sub(7, 5, 11) == 2
assert modm.mod_mul(7, 5, 11) == 2
assert modm.mod_pow(2, 10, 13) == 10
assert modm.mod_inverse(3, 11) == 4
assert thm.euler_totient(12) == 4
assert thm.fermat_little_theorem_valid(2, 5) is True
assert thm.euler_theorem_valid(2, 9) is True
assert cipher.caesar_encrypt('HELLO', 3) == 'KHOOR'
assert cipher.caesar_decrypt('KHOOR', 3) == 'HELLO'
msg = 'NUMBER'
enc = cipher.affine_encrypt(msg, 5, 8)
assert cipher.affine_decrypt(enc, 5, 8) == msg
keys = rsa.generate_rsa_keypair(50, 200)
msg_int = 42
cipher_int = rsa.rsa_encrypt(msg_int, keys['e'], keys['n'])
assert rsa.rsa_decrypt(cipher_int, keys['d'], keys['n']) == msg_int
assert thm.chinese_remainder_theorem([(2, 3), (3, 5)])[0] == 8
print('All core validation checks passed.')
