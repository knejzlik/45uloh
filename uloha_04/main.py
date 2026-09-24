from typing import List

def remove_first_element(lst: List[int]) -> int:
    """Odstraní první prvek ze seznamu a vrátí jej."""
    return lst.pop(0)

def main() -> None:
    items = [100, 200, 300]
    print(f"Před odstraněním: index 1 má hodnotu '{items[1]}'")

    removed = remove_first_element(items)
    print(f"Odstraněn prvek: {removed}")
    print(f"Po odstranění: index 1 má nyní hodnotu '{items[1]}'")
    print("Závěr: Po odstranění prvního prvku se indexy ostatních prvků posunuly.")

if __name__ == "__main__":
    main()
