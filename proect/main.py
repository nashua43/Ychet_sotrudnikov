"""
Главный модуль программы "Учёт сотрудников"
"""

from database import create_initial_data
from interface import show_main_menu, show_all_employees, add_employee, delete_employee, edit_employee
from reports import report1, report2, report3


def main():
    """Главная функция программы"""
    # Загружаем начальные данные
    employees = create_initial_data()

    while True:
        choice = show_main_menu()

        if choice == "1":
            show_all_employees(employees)
        elif choice == "2":
            employees = add_employee(employees)
        elif choice == "3":
            employees = delete_employee(employees)
        elif choice == "4":
            employees = edit_employee(employees)
        elif choice == "5":
            report1(employees)
        elif choice == "6":
            report2(employees)
        elif choice == "7":
            report3(employees)
        elif choice == "8":
            print("Выход из программы...")
            break
        else:
            print("Ошибка: выберите действие от 1 до 8!")


# Запуск программы
if __name__ == "__main__":
    main()