def main() -> None:
    s = {1, 2, 3}

    print(f"Původní set: {s}")
    s.add(2)  # Přidání stejné hodnoty podruhé
    print(f"Set po druhém přidání hodnoty 2: {s}")
    print("Závěr: Opakované přidání stejné hodnoty do setu je z pohledu jeho obsahu nerozeznatelné.")

if __name__ == "__main__":
    main()
