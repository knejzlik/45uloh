from typing import List, Set, Any

class UniquenessChecker:

    @staticmethod
    def preserve_order_unique(items: List[Any]) -> List[Any]:
        seen: Set[Any] = set()
        result: List[Any] = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

def main() -> None:
    data = ['jablko', 'banán', 'jablko', 'pomeranč']
    set_result = set(data)
    ordered_result = UniquenessChecker.preserve_order_unique(data)
    print(f'Původní data: {data}')
    print(f'Set (neumožňuje zachovat jistotu pořadí): {set_result}')
    print(f'List se zachováním pořadí: {ordered_result}')
    print('Závěr: Set NENÍ vždy vhodnější než list (např. když záleží na pořadí).')
if __name__ == '__main__':
    main()
