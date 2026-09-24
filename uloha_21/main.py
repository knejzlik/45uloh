def main() -> None:
    a = [1, 2, 3]
    b = [1, 2, 3]

    print(f"Platí a == b? {a == b}")
    print(f"Platí a is b? {a is b}")

    # Pokud změníme 'a'
    a.append(4)
    print(f"Po změně 'a': a = {a}, b = {b}")
    print("Závěr: Z toho, že a == b je True, neplyne, že lze proměnné bezpečně zaměnit (jsou to dvě různé instance).")

if __name__ == "__main__":
    main()
