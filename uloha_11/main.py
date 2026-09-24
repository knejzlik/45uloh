from typing import Tuple, List

def main() -> None:
    mutable_list: List[int] = [1, 2, 3]
    t: Tuple[List[int], str] = (mutable_list, 'skupina A')
    print(f'Původní tuple: {t}')
    t[0].append(4)
    print(f'Po změně vnitřního listu: {t}')
    print('Závěr: Immutable tuple může obsahovat mutable list a ten lze upravovat.')
if __name__ == '__main__':
    main()
