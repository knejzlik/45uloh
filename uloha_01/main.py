from typing import List, Set, Any

class UniquenessChecker:
    """Třída pro demonstrování zachování pořadí a unikátnosti u listu a setu."""

    @staticmethod
    def preserve_order_unique(items: List[Any]) -> List[Any]:
        """Vrátí seznam unikátních prvků se zachováním původního pořadí."""
        seen: Set[Any] = set()
        result: List[Any] = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

def main() -> None:
    data = ["jablko", "banán", "jablko", "pomeranč"]

    # Použití setu ztratí pořadí nebo ho nemusí zachovat
    set_result = set(data)

    # Použití čističe zachová pořadí
    ordered_result = UniquenessChecker.preserve_order_unique(data)

    print(f"Původní data: {data}")
    print(f"Set (neumožňuje zachovat jistotu pořadí): {set_result}")
    print(f"List se zachováním pořadí: {ordered_result}")
    print("Závěr: Set NENÍ vždy vhodnější než list (např. když záleží na pořadí).")

if __name__ == "__main__":
    main()
