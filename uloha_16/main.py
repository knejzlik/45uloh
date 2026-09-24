def main() -> None:
    student_grades = {}
    student_grades['Petr'] = 1
    print(f"Po vložení ('Petr': 1): {student_grades}")
    student_grades['Petr'] = 2
    print(f"Po vložení ('Petr': 2): {student_grades}")
    print(f'Počet položek ve slovníku: {len(student_grades)}')
    print('Závěr: Dvě různé položky nemohou mít v dictionary stejný klíč. Dochází k přepsání.')
if __name__ == '__main__':
    main()
