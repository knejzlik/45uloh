def main() -> None:
    scores = {'Alice': 100, 'Bob': 100, 'Charlie': 100}
    print(f'Slovník: {scores}')
    print(f'Počet položek ve slovníku: {len(scores)}')
    print('Závěr: Různé klíče mohou mít stejnou hodnotu, žádná položka se neodstraňuje.')
if __name__ == '__main__':
    main()
