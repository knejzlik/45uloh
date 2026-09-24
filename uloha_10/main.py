import time

n = 500_000
data_list = list(range(n))
data_set = set(range(n))
target = 499_999

t0 = time.perf_counter()
_ = target in data_list
t_list = time.perf_counter() - t0

t0 = time.perf_counter()
_ = target in data_set
t_set = time.perf_counter() - t0

print(f"Vyhledání v listu bez znalosti pozice: {t_list:.6f} s")
print(f"Vyhledání v setu bez znalosti pozice:  {t_set:.6f} s")
