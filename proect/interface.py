"""
Модуль пользовательского интерфейса
"""

from validation import get_input, validate_name, validate_department, validate_position
from validation import validate_number, validate_salary, validate_day


def show_all_employees(employees):
    """Показать всех сотрудников"""
    if not employees:
        print("Список сотрудников пуст!")
        return

    print("\n" + "=" * 100)
    print("СПИСОК ВСЕХ СОТРУДНИКОВ")
    print("=" * 100)
    print(f"{'№':3} | {'ФИО':30} | {'Дата рождения':15} | {'Отдел':15} | {'Должность':20} | {'Оклад':10} | {'Стаж':5}")
    print("-" * 100)

    for i, emp in enumerate(employees, 1):
        date = f"{emp['день']:02d}.{emp['месяц']:02d}.{emp['год']}"
        name = f"{emp['фамилия']} {emp['имя']} {emp['отчество']}"
        print(
            f"{i:3} | {name:30} | {date:15} | {emp['отдел']:15} | {emp['должность']:20} | {emp['оклад']:10} | {emp['стаж']:5}")

    print(f"Всего: {len(employees)}")
    print("=" * 100)


def add_employee(employees):
    """Добавить нового сотрудника"""
    print("\n" + "=" * 50)
    print("ДОБАВЛЕНИЕ СОТРУДНИКА")
    print("=" * 50)

    # Ввод данных с проверкой
    last_name = get_input("Фамилия: ", validate_name)
    first_name = get_input("Имя: ", validate_name)
    middle_name = get_input("Отчество: ", validate_name)

    year = int(get_input("Год рождения (1900-2023): ", lambda x: validate_number(x, 1900, 2023, "Год")))
    month = int(get_input("Месяц (1-12): ", lambda x: validate_number(x, 1, 12, "Месяц")))

    # День с учетом месяца и года
    while True:
        day_str = get_input("День (1-31): ")
        if validate_day(day_str, year, month):
            day = int(day_str)
            break

    department = get_input("Отдел: ", validate_department)
    position = get_input("Должность: ", validate_position)

    salary = int(get_input("Оклад: ", validate_salary))
    experience = int(get_input("Стаж (лет): ", lambda x: validate_number(x, 0, 60, "Стаж")))

    # Создание сотрудника
    new_emp = {
        "фамилия": last_name, "имя": first_name, "отчество": middle_name,
        "год": year, "месяц": month, "день": day,
        "отдел": department, "должность": position,
        "оклад": salary, "стаж": experience
    }

    employees.append(new_emp)
    print(f"\nСотрудник {last_name} {first_name} добавлен!")
    return employees


def delete_employee(employees):
    """Удалить сотрудника"""
    if not employees:
        print("Список пуст!")
        return employees

    show_all_employees(employees)

    while True:
        choice = input("\nВведите номер сотрудника для удаления (0-отмена): ").strip()

        # Проверка на пустой ввод
        if not choice:
            print("Ошибка: поле не может быть пустым!")
            continue

        # Проверка на отмену
        if choice == "0":
            return employees

        # Проверка, что введено число
        if not choice.isdigit():
            print("Ошибка: введите число!")
            continue

        # Проверка, что число в допустимом диапазоне
        num = int(choice)
        if num < 1 or num > len(employees):
            print(f"Ошибка: введите число от 1 до {len(employees)}!")
            continue

        # Подтверждение удаления
        emp = employees[num - 1]
        confirm = input(
            f"Вы уверены, что хотите удалить сотрудника {emp['фамилия']} {emp['имя']}? (да/нет): ").strip().lower()

        # Проверка подтверждения
        if confirm not in ['да', 'д', 'yes', 'y']:
            print("Удаление отменено.")
            return employees

        # Удаление
        del employees[num - 1]
        print(f"Сотрудник {emp['фамилия']} {emp['имя']} удален!")
        return employees


def edit_employee(employees):
    """Изменить данные сотрудника"""
    if not employees:
        print("Список пуст!")
        return employees

    show_all_employees(employees)

    while True:
        choice = input("\nВведите номер сотрудника для редактирования (0-отмена): ").strip()

        # Проверка на пустой ввод
        if not choice:
            print("Ошибка: поле не может быть пустым!")
            continue

        # Проверка на отмену
        if choice == "0":
            return employees

        # Проверка, что введено число
        if not choice.isdigit():
            print("Ошибка: введите число!")
            continue

        # Проверка, что число в допустимом диапазоне
        num = int(choice)
        if num < 1 or num > len(employees):
            print(f"Ошибка: введите число от 1 до {len(employees)}!")
            continue

        # Редактирование сотрудника
        emp = employees[num - 1]
        print(f"\nРедактирование: {emp['фамилия']} {emp['имя']}")
        print("(оставьте пустым чтобы не менять)")

        # Редактируем каждое поле
        fields = [
            ("Фамилия", "фамилия", validate_name),
            ("Имя", "имя", validate_name),
            ("Отчество", "отчество", validate_name),
            ("Год", "год", lambda x: validate_number(x, 1900, 2023, "Год")),
            ("Месяц", "месяц", lambda x: validate_number(x, 1, 12, "Месяц")),
            ("Оклад", "оклад", validate_salary),
            ("Стаж", "стаж", lambda x: validate_number(x, 0, 60, "Стаж"))
        ]

        for display_name, field_name, validation in fields:
            while True:
                new_val = input(f"{display_name} [{emp[field_name]}]: ").strip()
                if not new_val:
                    break  # Оставляем старое значение
                if validation(new_val):
                    # Преобразуем в число если нужно
                    if field_name in ['год', 'месяц', 'оклад', 'стаж']:
                        emp[field_name] = int(new_val)
                    else:
                        emp[field_name] = new_val
                    break
                else:
                    print(f"Некорректное значение. Попробуйте еще раз или оставьте пустым.")

        # День отдельно, так как зависит от года и месяца
        while True:
            new_day = input(f"День [{emp['день']}]: ").strip()
            if not new_day:
                break
            if validate_day(new_day, emp['год'], emp['месяц']):
                emp['день'] = int(new_day)
                break
            else:
                print("Некорректный день. Попробуйте еще раз или оставьте пустым.")

        # Отдел с проверкой
        while True:
            new_dept = input(f"Отдел [{emp['отдел']}]: ").strip()
            if not new_dept:
                break
            if validate_department(new_dept):
                emp['отдел'] = new_dept
                break
            else:
                print("Некорректный отдел. Попробуйте еще раз или оставьте пустым.")

        # Должность с проверкой
        while True:
            new_pos = input(f"Должность [{emp['должность']}]: ").strip()
            if not new_pos:
                break
            if validate_position(new_pos):
                emp['должность'] = new_pos
                break
            else:
                print("Некорректная должность. Попробуйте еще раз или оставьте пустым.")

        print("Данные обновлены!")
        return employees


def show_main_menu():
    """Показать главное меню"""
    print("\n" + "=" * 50)
    print("ПРОГРАММА 'УЧЁТ СОТРУДНИКОВ'")
    print("=" * 50)
    print("1. Показать всех сотрудников")
    print("2. Добавить сотрудника")
    print("3. Удалить сотрудника")
    print("4. Изменить данные сотрудника")
    print("5. Отчет 1: Сортировка по году рождения, стажу, фамилии")
    print("6. Отчет 2: Сотрудники отдела (сортировка по окладу, фамилии)")
    print("7. Отчет 3: Сотрудники с окладом выше среднего")
    print("8. Выход")
    print("=" * 50)

    return input("Выберите действие (1-8): ").strip()