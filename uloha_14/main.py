def main() -> None:
    data_list = [1, 2, 3]
    data_tuple = (1, 2, 3)
    data_set = {1, 2, 3}
    print(f'Typ data_list:  {type(data_list)}')
    print(f'Typ data_tuple: {type(data_tuple)}')
    print(f'Typ data_set:   {type(data_set)}')
    print('Závěr: Kolekce se stejným obsahem nemusí mít stejný datový typ.')
if __name__ == '__main__':
    main()
