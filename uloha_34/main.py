def main() -> None:
    # Malý počet prvků (3 prvky)
    # 1. Potřebujeme mapování klíč-hodnota -> dict
    user_role = {"id": 1, "role": "admin"}

    # 2. Potřebujeme pouhou množinu unikátních ID -> set
    ids = {1, 2, 3}

    # 3. Potřebujeme sekvenci kroků -> list
    steps = ["step1", "step2", "step3"]

    print(f"Dict: {user_role}")
    print(f"Set:  {ids}")
    print(f"List: {steps}")
    print("Závěr: Vhodnost kolekce závisí na operacích a sémantice, nikoli na počtu uložných prvků.")

if __name__ == "__main__":
    main()
