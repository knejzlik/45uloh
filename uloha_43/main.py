def main() -> None:
    items = [10, 20, 30, 40, 50]

    # Hledání prvku na konci
    end_val = 50
    # Hledání prvku, který v seznamu není
    missing_val = 99

    # V obou případech lineární vyhledávání musí projít VŠECH N prvků
    print(f"Hledání prvku na konci ({end_val}): nejpříznivější nejhorší případ O(n)")
    print(f"Hledání neexistujícího prvku ({missing_val}): také O(n)")
    print("Závěr: Obě operace mají v nejhorším případě asymptotickou složitost O(n).")

if __name__ == "__main__":
    main()
