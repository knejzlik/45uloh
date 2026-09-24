def main() -> None:
    # Slovník s řetězcovými klíči
    user_data = {"name": "Jan", "age": 18}

    try:
        first_item = user_data[0]  # type: ignore
        print(f"Položka na klíči 0: {first_item}")
    except KeyError as e:
        print(f"Vyvolána výjimka KeyError: klíč {e} neexistuje.")
        print("Závěr: Slovník neumožňuje vypsat 'první prvek' pomocí číselného indexu 0, pokud 0 není existující klíč.")

if __name__ == "__main__":
    main()
