# ziltrix-sch-core
Ziltrix — Sentinel Cognitive Hybridiser. Where Intelligence Becomes Intelligent.

## Usage

Python examples:

```python
from ziltrix_sch_core import fib, lucas, phi, binet
from ziltrix_sch_core import to_balanced_ternary, from_balanced_ternary
from ziltrix_sch_core import entropy_bytes, deterministic_kdf

print(fib(10))           # 55
print(lucas(10))         # 123
print(phi())             # Decimal('1.6180...')
print(binet(20))         # 6765 (matches fib(20))

s = to_balanced_ternary(-42)  # e.g., 'T1T10'
print(s, from_balanced_ternary(s))

key = deterministic_kdf("my-seed", "ziltrix", out_len=32)
print(len(key))          # 32
```
