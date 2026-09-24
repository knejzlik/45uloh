import time

def main() -> None:
    # Velmi malý vstup
    small_list = [1, 2]
    small_set = {1, 2}

    target = 2

    t0 = time.perf_counter()
    _ = target in small_list
    t_list = time.perf_counter() - t0

    t0 = time.perf_counter()
    _ = target in small_set
    t_set = time.perf_counter() - t0

    print(f"Čas v listu (2 prvky): {t_list:.8f} s")
    print(f"Čas v setu (2 prvky):  {t_set:.8f} s")
    print("Závěr: Jedno měření pro konkrétní vstup nedokazuje, že set bude vždy rychlejší pro každý možný vstup.")

if __name__ == "__main__":
    main()
