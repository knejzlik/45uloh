def main() -> None:
    s = {10, 20, 30}

    try:
        _ = s[0]  # type: ignore
    except TypeError as e:
        print(f"Chyba při pokusu o indexování setu: {e}")
        print("Závěr: Set nepodporuje indexování a není náhradou za list pro přístup podle pořadí.")

if __name__ == "__main__":
    main()
