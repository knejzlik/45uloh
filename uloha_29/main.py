from typing import Dict, Tuple

def main() -> None:
    # Použití tuple (zeměpisné souřadnice) jako klíče
    locations: Dict[Tuple[float, float], str] = {
        (50.0755, 14.4378): "Praha",
        (49.1951, 16.6068): "Brno"
    }

    prague = locations[(50.0755, 14.4378)]
    print(f"Lokace na souřadnicích (50.0755, 14.4378): {prague}")
    print("Závěr: Tuple lze použít jako klíč v dictionary, protože je immutable a hashovatelný.")

if __name__ == "__main__":
    main()
