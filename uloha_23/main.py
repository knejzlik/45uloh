def main() -> None:
    text = "Python"
    lst = ['P', 'y', 't', 'h', 'o', 'n']

    print(f"text[0] = '{text[0]}', lst[0] = '{lst[0]}'")
    print(f"text[-1] = '{text[-1]}', lst[-1] = '{lst[-1]}'")
    print(f"text[1:4] = '{text[1:4]}', lst[1:4] = {lst[1:4]}")
    print("Závěr: String se z hlediska indexování a výřezů chová velmi podobně jako list.")

if __name__ == "__main__":
    main()
