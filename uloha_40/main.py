import time

small_list = [1, 2]
small_set = {1, 2}

t0 = time.perf_counter()
_ = 2 in small_list
t_list = time.perf_counter() - t0

t0 = time.perf_counter()
_ = 2 in small_set
t_set = time.perf_counter() - t0

print(f"Čas list: {t_list:.8f} s, čas set: {t_set:.8f} s")
