def main() -> None:
    keys = ['id1', 'id2', 'id3']
    vals = ['Alice', 'Bob', 'Charlie']
    idx = keys.index('id2')
    res_list = vals[idx]
    d = {'id1': 'Alice', 'id2': 'Bob', 'id3': 'Charlie'}
    res_dict = d['id2']
    print(f'Výsledek z listů: {res_list}')
    print(f'Výsledek ze slovníku: {res_dict}')
    print('Závěr: Používat pouze list je neefektivní a nepřehledné. Různé kolekce mají nezastupitelný význam.')
if __name__ == '__main__':
    main()
