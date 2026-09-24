import time

n = 500_000
target = -1

large_list = list(range(n))
large_set = set(range(n))

t0 = time.perf_counter()
_ = target in large_list
t_list = time.perf_counter() - t0

t0 = time.perf_counter()
_ = target in large_set
t_set = time.perf_counter() - t0

print(f"Čas vyhledávání v listu: {t_list:.6f} s")
print(f"Čas vyhledávání v setu:  {t_set:.6f} s")
