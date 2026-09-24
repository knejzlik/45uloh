def main() -> None:
    elements = ['a', 'b', 'a', 'a', 'c']
    s = set(elements)
    print(f'Původní prvky: {elements}')
    print(f'Množina: {s}')
    print(f"Obsahuje set počet výskytů 'a'? NE (množina má pouze prvek 'a', délka setu je {len(s)}).")
if __name__ == '__main__':
    main()
