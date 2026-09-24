from typing import List

def update_first_element(lst: List[int], new_val: int) -> None:
    lst[0] = new_val

def main() -> None:
    numbers = [10, 20, 30]
    print(f"Původní list: {numbers}")

    update_first_element(numbers, 99)
    print(f"Upravený list: {numbers}")
    print("Závěr: Pokud potřebujeme měnit hodnoty prvků na pozicích (bez přidávání/mazání), je list vhodnější než tuple.")

if __name__ == "__main__":
    main()
