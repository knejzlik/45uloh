def main() -> None:
    coords_a = [10, 20]  # x = 10, y = 20
    coords_b = [20, 10]  # x = 20, y = 10

    print(f"Souřadnice A: {coords_a}")
    print(f"Souřadnice B: {coords_b}")
    print(f"Rovnají se kolekce podle == ? {coords_a == coords_b}")
    print("Závěr: Stejné hodnoty v jiném pořadí reprezentují odlišnou informaci.")

if __name__ == "__main__":
    main()
