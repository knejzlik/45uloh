def main() -> None:
    original_list = [3, 1, 2, 1, 3]
    converted_set = set(original_list)
    restored_list = list(converted_set)
    print(f'Původní list:        {original_list}')
    print(f'Převod list->set->list: {restored_list}')
    print(f'Jsou seznamy identické? {original_list == restored_list}')
    print('Závěr: Převedením na set a zpět se mohou ztratit duplicity a změnit pořadí.')
if __name__ == '__main__':
    main()
