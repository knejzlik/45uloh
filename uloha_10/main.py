import time

def main() -> None:
    n = 500000
    data_list = list(range(n))
    data_set = set(range(n))
    target = 499999
    t0 = time.perf_counter()
    _ = target in data_list
    t_list = time.perf_counter() - t0
    t0 = time.perf_counter()
    _ = target in data_set
    t_set = time.perf_counter() - t0
    print(f'Hledání v listu bez znalosti pozice: {t_list:.6f} s (O(n))')
    print(f'Hledání v setu bez znalosti pozice:  {t_set:.6f} s (O(1))')
    print('Závěr: List NEPOSKYTUJE stejně asymptoticky efektivní přístup jako set.')
if __name__ == '__main__':
    main()
