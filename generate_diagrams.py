from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

out = Path(__file__).resolve().parent / 'assets' / 'diagrams'
out.mkdir(parents=True, exist_ok=True)

# Prime distribution
limit = 100
primes = []
for n in range(2, limit + 1):
    ok = True
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            ok = False
            break
    if ok:
        primes.append(n)

plt.figure(figsize=(8, 5))
plt.scatter(primes, [1] * len(primes), s=12, color='darkgreen')
plt.title('Prime distribution up to 100')
plt.xlabel('Integer n')
plt.yticks([])
plt.tight_layout()
plt.savefig(out / 'prime_distribution.png', dpi=200)
plt.close()

# Euclidean algorithm example
plt.figure(figsize=(8, 5))
a, b = 252, 105
pairs = []
while b != 0:
    pairs.append((a, b))
    a, b = b, a % b
plt.plot([x for x, _ in pairs], [y for _, y in pairs], marker='o', linestyle='--', color='royalblue')
plt.title('Euclidean algorithm steps for gcd(252, 105)')
plt.xlabel('Current a')
plt.ylabel('Current b')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(out / 'euclidean_algorithm.png', dpi=200)
plt.close()

# Modular patterns
x = np.arange(0, 13)
y = (7 * x) % 13
plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', color='crimson')
plt.title('Pattern of 7x mod 13')
plt.xlabel('x')
plt.ylabel('(7x) mod 13')
plt.xticks(x)
plt.yticks(np.arange(0, 13, 1))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(out / 'modular_patterns.png', dpi=200)
plt.close()

# RSA workflow
plt.figure(figsize=(8, 5))
flow = [
    'Choose p, q',
    'Compute n = p q',
    'Compute phi(n)',
    'Choose e',
    'Compute d',
    'Encrypt',
    'Decrypt',
]
for i, label in enumerate(flow):
    plt.text(0.5, 0.8 - i * 0.12, label, fontsize=12, ha='center', va='center', bbox=dict(boxstyle='round', facecolor='lightsteelblue', edgecolor='navy'))
plt.axis('off')
plt.title('Educational RSA workflow')
plt.tight_layout()
plt.savefig(out / 'rsa_workflow.png', dpi=200)
plt.close()

print('Generated diagrams:', sorted(str(p.name) for p in out.glob('*.png')))
