def main() -> None:
    lst = [1, 2, 3]
    tpl = (1, 2, 3)
    print(f'Indexování lst[0]: {lst[0]}')
    print(f'Indexování tpl[0]: {tpl[0]}')
    lst[0] = 99
    print(f'Upravený list: {lst}')
    try:
        tpl[0] = 99
    except TypeError as e:
        print(f'Tuple nedovoluje změnu prvku: {e}')
    print('Závěr: Podpora indexování neznamená stejné možnosti změny obsahu.')
if __name__ == '__main__':
    main()
