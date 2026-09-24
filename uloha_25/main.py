def main() -> None:
    user_catalog = {
        "usr_101": {"name": "Alice", "role": "admin"},
        "usr_102": {"name": "Bob", "role": "user"}
    }

    user_id = "usr_101"
    user_info = user_catalog.get(user_id)

    print(f"ID: {user_id} -> Hodnota: {user_info}")
    print("Závěr: Slovník uchovává jak identifikátor (klíč), tak k němu příslušnou hodnotu.")

if __name__ == "__main__":
    main()
