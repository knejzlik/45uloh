def main() -> None:
    data_list = [1, 2, 2, 3]
    data_set = {1, 2, 3}
    print(f'List: {data_list} (obsahuje informaci o četnosti prvku 2)')
    print(f'Set:  {data_set} (obsahuje pouze informaci o existenci)')
    print('Závěr: I při stejných obsažených hodnotách nenesou stejnou informaci.')
if __name__ == '__main__':
    main()
