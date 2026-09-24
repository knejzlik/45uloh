import time

list_small = list(range(100_000))
list_large = list(range(200_000))

t0 = time.perf_counter()
len1 = len(list_small)
t1 = time.perf_counter() - t0

t0 = time.perf_counter()
len2 = len(list_large)
t2 = time.perf_counter() - t0

print(f"len() pro 100k: {t1:.8f} s")
print(f"len() pro 200k: {t2:.8f} s")
