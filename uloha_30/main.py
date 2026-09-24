def main() -> None:
    nested_list = [1, 2]
    immutable_tuple = (nested_list, 'konstanta')
    print(f'Původní tuple: {immutable_tuple}')
    immutable_tuple[0].append(3)
    print(f'Tuple po modifikaci vnitřního listu: {immutable_tuple}')
    print('Závěr: To, že kolekce neumožňuje měnit své prvky, neznamená, že všechny vnořené objekty jsou immutable.')
if __name__ == '__main__':
    main()
