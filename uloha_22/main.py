def main() -> None:
    a = [10, 20]
    b = a
    print(f'Platí a is b? {a is b}')
    a.append(30)
    print(f'Obsah b po změně v a: {b}')
    print('Závěr: Pokud a is b je True, změna přes a je okamžitě viditelná i přes b.')
if __name__ == '__main__':
    main()
