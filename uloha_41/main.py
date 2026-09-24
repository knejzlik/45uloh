import time

small_list = list(range(10))
small_set = set(range(10))

large_list = list(range(500_000))
large_set = set(range(500_000))

t0 = time.perf_counter()
_ = -1 in small_list
t_l_small = time.perf_counter() - t0

t0 = time.perf_counter()
_ = -1 in small_set
t_s_small = time.perf_counter() - t0

t0 = time.perf_counter()
_ = -1 in large_list
t_l_large = time.perf_counter() - t0

t0 = time.perf_counter()
_ = -1 in large_set
t_s_large = time.perf_counter() - t0

print(f"Small (10): List={t_l_small:.7f}s, Set={t_s_small:.7f}s")
print(f"Large (500k): List={t_l_large:.7f}s, Set={t_s_large:.7f}s")
