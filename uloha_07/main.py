import time
from typing import Container

def measure_lookup_time(container: Container[int], value: int) -> float:
    start = time.perf_counter()
    _ = value in container
    end = time.perf_counter()
    return end - start

def main() -> None:
    n = 1000000
    target = -1
    large_list = list(range(n))
    large_set = set(range(n))
    time_list = measure_lookup_time(large_list, target)
    time_set = measure_lookup_time(large_set, target)
    print(f'Čas vyhledávání v listu ({n} prvků): {time_list:.6f} s')
    print(f'Čas vyhledávání v setu ({n} prvků):  {time_set:.6f} s')
    print('Závěr: Pro opakované zjišťování přítomnosti je set výrazně efektivnější.')
if __name__ == '__main__':
    main()
