from typing import Tuple, List

def main() -> None:
    inner_list: List[int] = [1, 2]
    t: Tuple[List[int], int] = (inner_list, 100)

    tuple_id_before = id(t)

    # Úprava vnitřního listu
    t[0].append(3)

    tuple_id_after = id(t)

    print(f"ID tuple před změnou: {tuple_id_before}")
    print(f"ID tuple po změně:   {tuple_id_after}")
    print(f"Jsou ID stejná? {tuple_id_before == tuple_id_after}")
    print("Závěr: Změna obsahu vnitřního listu nezměnila samotný tuple (jeho identita/odkaz zůstává stejný).")

if __name__ == "__main__":
    main()
