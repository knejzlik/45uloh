from typing import Tuple

def main() -> None:
    data: Tuple[int, int, int] = (10, 20, 30)
    print(f'Původní tuple: {data}')
    try:
        data[0] = 99
    except TypeError as e:
        print(f'Chyba při pokusu o změnu: {e}')
        print('Závěr: Tuple je neměnný (immutable).')
if __name__ == '__main__':
    main()
