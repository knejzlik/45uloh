import time

n = 500_000
data = list(range(n))
target_idx = n - 1
target_val = data[target_idx]

t0 = time.perf_counter()
_ = data[target_idx]
t_idx = time.perf_counter() - t0

t0 = time.perf_counter()
_ = target_val in data
t_in = time.perf_counter() - t0

print(f"Přístup indexem lst[{target_idx}]: {t_idx:.8f} s (O(1))")
print(f"Vyhledání operátorem in:      {t_in:.8f} s (O(n))")
