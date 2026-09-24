from typing import List, Set

class FastTracker:

    def __init__(self) -> None:
        self._history: List[int] = []
        self._lookup: Set[int] = set()

    def add(self, val: int) -> None:
        self._history.append(val)
        self._lookup.add(val)

    def contains(self, val: int) -> bool:
        return val in self._lookup

    def get_all(self) -> List[int]:
        return self._history

def main() -> None:
    tracker = FastTracker()
    tracker.add(10)
    tracker.add(20)
    tracker.add(10)
    print(f'Všechny výskyty (list): {tracker.get_all()}')
    print(f'Rychlé ověření existence 20 (set): {tracker.contains(20)}')
    print('Závěr: Pro rychlé vyhledávání i zachování opakování je vhodné zkombinovat více kolekcí.')
if __name__ == '__main__':
    main()
