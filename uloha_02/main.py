from typing import List, Set, Any

def try_insert_to_set(item: Any) -> bool:
    try:
        s: Set[Any] = set()
        s.add(item)
        return True
    except TypeError:
        return False

def main() -> None:
    mutable_item = [1, 2, 3]
    lst: List[Any] = []
    lst.append(mutable_item)
    can_insert_set = try_insert_to_set(mutable_item)
    print(f'Vložení mutable listu do listu: ÚSPĚCH (lst = {lst})')
    print(f"Vložení mutable listu do setu: {('ÚSPĚCH' if can_insert_set else 'SELHALO (TypeError)')}")
    print('Závěr: Objekty, které lze vložit do listu (např. mutable listy), nelze vždy vložit do setu.')
if __name__ == '__main__':
    main()
