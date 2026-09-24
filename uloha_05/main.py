def main() -> None:
    lst = [10, 20, 30, 40]
    d = {0: 10, 1: 20, 2: 30, 3: 40}
    print(f'List slicing lst[1:3]: {lst[1:3]}')
    try:
        _ = d[1:3]
    except (TypeError, KeyError) as e:
        print(f'Dict slicing d[1:3] vyvolal očekávanou výjimku {type(e).__name__}: {e}')
        print('Závěr: Slovník nemůže plně nahradit list bez ztráty vlastností (např. slicing).')
if __name__ == '__main__':
    main()
