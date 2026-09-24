def main() -> None:
    my_list = [10, 20, 30]
    my_set = {10, 20, 30}
    target = 20
    print(f'{target} in my_list: {target in my_list}')
    print(f'{target} in my_set:  {target in my_set}')
    print("Závěr: Operátor 'in' funguje jak pro list, tak pro set.")
if __name__ == '__main__':
    main()
