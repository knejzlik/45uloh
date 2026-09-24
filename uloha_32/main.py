def main() -> None:
    data = [10, 20, 30, 40]
    original_len = len(data)
    dedup_len = len(set(data))
    print(f'Původní délka: {original_len}, Délka po deduplikaci: {dedup_len}')
    if original_len == dedup_len:
        print('Usuzujeme: Všechny prvky v původním seznamu byly unikatní.')
if __name__ == '__main__':
    main()
