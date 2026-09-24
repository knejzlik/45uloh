def main() -> None:
    user_role = {'id': 1, 'role': 'admin'}
    ids = {1, 2, 3}
    steps = ['step1', 'step2', 'step3']
    print(f'Dict: {user_role}')
    print(f'Set:  {ids}')
    print(f'List: {steps}')
    print('Závěr: Vhodnost kolekce závisí na operacích a sémantice, nikoli na počtu uložných prvků.')
if __name__ == '__main__':
    main()
