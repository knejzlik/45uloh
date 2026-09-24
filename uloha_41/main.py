import time

def measure_in(container, val):
    t0 = time.perf_counter()
    _ = val in container
    return time.perf_counter() - t0

def main() -> None:
    small_n = 10
    small_list = list(range(small_n))
    small_set = set(range(small_n))
    t_list_small = measure_in(small_list, -1)
    t_set_small = measure_in(small_set, -1)
    large_n = 500000
    large_list = list(range(large_n))
    large_set = set(range(large_n))
    t_list_large = measure_in(large_list, -1)
    t_set_large = measure_in(large_set, -1)
    print(f'Pro N={small_n}: List={t_list_small:.7f}s, Set={t_set_small:.7f}s')
    print(f'Pro N={large_n}: List={t_list_large:.7f}s, Set={t_set_large:.7f}s')
    print('Závěr: S rostoucím N se poměr času t_list / t_set dramaticky zvyšuje.')
if __name__ == '__main__':
    main()
