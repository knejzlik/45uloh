def main() -> None:
    set_a = {1, 2, 3, 4}
    set_b = {4, 3, 2, 1}
    are_equal = set_a == set_b
    print(f'Set A: {set_a}')
    print(f'Set B: {set_b}')
    print(f'Jsou si množiny rovny? {are_equal}')
    print('Závěr: Dvě množiny se rovnají bez ohledu na pořadí vkládání prvků.')
if __name__ == '__main__':
    main()
