def main() -> None:
    scores = [10, 20, 20, 30, 10, 40]
    scores_set = set(scores)

    print(f"Původní seznam (délka {len(scores)}): {scores}")
    print(f"Množina (délka {len(scores_set)}): {scores_set}")
    print("Závěr: Převodem na set došlo ke ztrátě informací o počtu výskytů duplicitních hodnot.")

if __name__ == "__main__":
    main()
