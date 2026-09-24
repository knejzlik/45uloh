def main() -> None:
    unique_list = [1, 2, 3, 4, 5]
    unique_set = {1, 2, 3, 4, 5}
    first_item_list = unique_list[0]
    try:
        _ = unique_set[0]
    except TypeError as e:
        print(f'Chyba při přístupu k setu indexem: {e}')
    print(f'První prvek v listu přes index 0: {first_item_list}')
    print('Závěr: I když list obsahuje pouze unikátní hodnoty, má odlišné vlastnosti než set (např. indexování).')
if __name__ == '__main__':
    main()
