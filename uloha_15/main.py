def main() -> None:
    duplicates = [1, 1, 1, 2]
    nested_list = [[1, 2], [3, 4]]
    print(f'List s duplicitami: {duplicates}')
    print(f'List s vnořenými seznamy: {nested_list}')
    print('Závěr: List může reprezentovat duplicity a unhashable struktury, které set reprezentovat nedokáže.')
if __name__ == '__main__':
    main()
