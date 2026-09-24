def main() -> None:
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(f'Na počátku a == b? {a == b}')
    a.append(100)
    print(f'Po změně a: a = {a}, b = {b}')
    print(f'Platí stále a == b? {a == b}')
    print('Závěr: Dvě nezávislé kolekce se stejným obsahem se po modifikaci jedné z nich liší.')
if __name__ == '__main__':
    main()
