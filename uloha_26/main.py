def main() -> None:
    shared_object = {"status": "ACTIVE"}

    # Seznam s 10 odkazy na tentýž objekt
    references_list = [shared_object] * 10

    print(f"Před změnou: index 0 status = {references_list[0]['status']}")

    # Změna objektu na indexu 0
    references_list[0]["status"] = "INACTIVE"

    print(f"Po změně: index 9 status = {references_list[9]['status']}")
    print("Závěr: Změna sdíleného mutable objektu se projevila na všech 10 místech v seznamu.")

if __name__ == "__main__":
    main()
