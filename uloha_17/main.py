def main() -> None:
    s = {'jablko', 'hruška', 'banán', 'ananas', 'pomeranč'}
    elements = list(s)
    print(f'Prvky množiny při iteraci: {elements}')
    print('Závěr: Množina negarantuje pořadí prvků při výpisu ani stabilní pořadí napříč spuštěními.')
if __name__ == '__main__':
    main()
