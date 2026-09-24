import time

def main() -> None:
    n = 1000000
    data = list(range(n))
    target_idx = n - 1
    target_val = data[target_idx]
    t0 = time.perf_counter()
    _ = data[target_idx]
    t_index = time.perf_counter() - t0
    t0 = time.perf_counter()
    _ = target_val in data
    t_in = time.perf_counter() - t0
    print(f'Přístup indexem lst[{target_idx}]: {t_index:.8f} s (O(1))')
    print(f"Vyhledání operátorem 'in':    {t_in:.8f} s (O(n))")
    print("Závěr: Přístup podle indexu (O(1)) a vyhledávání pomocí 'in' (O(n)) NEMAJÍ stejnou časovou složitost.")
if __name__ == '__main__':
    main()
