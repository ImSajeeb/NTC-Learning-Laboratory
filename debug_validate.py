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

print('loading arith', flush=True)
ar = load_module('arith', root / '01_Mathematical_Foundations' / 'arithmetic_operations.py')
print('loaded arith', flush=True)
print(ar.is_divisible(48,6), flush=True)
print('loading pt', flush=True)
pt = load_module('pt', root / '02_Prime_Number_Analysis' / 'prime_tools.py')
print('loaded pt', flush=True)
print(pt.is_prime(17), flush=True)
print('loading gcdm', flush=True)
gcdm = load_module('gcdm', root / '03_GCD_and_Diophantine_Equations' / 'euclidean_methods.py')
print('loaded gcdm', flush=True)
print(gcdm.gcd(48,18), flush=True)
print('loading modm', flush=True)
modm = load_module('modm', root / '04_Modular_Systems' / 'modular_operations.py')
print('loaded modm', flush=True)
print(modm.mod_inverse(3,11), flush=True)
print('loading thm', flush=True)
thm = load_module('thm', root / '05_Number_Theory_Theorems' / 'theorem_implementations.py')
print('loaded thm', flush=True)
print(thm.euler_totient(12), flush=True)
print('loading cipher', flush=True)
cipher = load_module('cipher', root / '06_Cryptographic_Methods' / 'classical_ciphers.py')
print('loaded cipher', flush=True)
print(cipher.caesar_encrypt('HELLO',3), flush=True)
print('loading rsa', flush=True)
rsa = load_module('rsa', root / '07_Public_Key_Cryptography' / 'rsa_engine.py')
print('loaded rsa', flush=True)
print(rsa.generate_rsa_keypair(50, 200), flush=True)
