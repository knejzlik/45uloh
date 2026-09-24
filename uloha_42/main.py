import time

def main() -> None:
    list_small = list(range(100000))
    list_large = list(range(200000))
    t0 = time.perf_counter()
    len_small = len(list_small)
    t_small = time.perf_counter() - t0
    t0 = time.perf_counter()
    len_large = len(list_large)
    t_large = time.perf_counter() - t0
    print(f'len() pro 100k prvků: {t_small:.8f} s')
    print(f'len() pro 200k prvků: {t_large:.8f} s')
    print('Závěr: Zdvojnásobení počtu prvků NEZDVOJNÁSOBÍ čas pro operace s O(1) složitostí (např. len).')
if __name__ == '__main__':
    main()
