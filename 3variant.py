# Программа "Учёт сотрудников"
# Вариант 3

def main():
    """Главная функция программы"""
    employees = [
        {"фамилия": "Иванов", "имя": "Иван", "отчество": "Иванович", "год": 1985, "месяц": 5, "день": 15, "отдел": "ИТ",
         "должность": "Программист", "оклад": 80000, "стаж": 10},
        {"фамилия": "Петров", "имя": "Петр", "отчество": "Петрович", "год": 1990, "месяц": 8, "день": 22,
         "отдел": "Бухгалтерия", "должность": "Бухгалтер", "оклад": 60000, "стаж": 5},
        {"фамилия": "Сидоров", "имя": "Сидор", "отчество": "Сидорович", "год": 1988, "месяц": 3, "день": 10,
         "отдел": "ИТ", "должность": "Аналитик", "оклад": 90000, "стаж": 8},
        {"фамилия": "Кузнецов", "имя": "Алексей", "отчество": "Сергеевич", "год": 1995, "месяц": 11, "день": 5,
         "отдел": "Отдел кадров", "должность": "Менеджер", "оклад": 55000, "стаж": 3},
        {"фамилия": "Смирнова", "имя": "Ольга", "отчество": "Александровна", "год": 1992, "месяц": 7, "день": 30,
         "отдел": "Бухгалтерия", "должность": "Главный бухгалтер", "оклад": 95000, "стаж": 7},
        {"фамилия": "Васильев", "имя": "Василий", "отчество": "Васильевич", "год": 1980, "месяц": 1, "день": 20,
         "отдел": "Производство", "должность": "Инженер", "оклад": 75000, "стаж": 15},
        {"фамилия": "Николаев", "имя": "Николай", "отчество": "Николаевич", "год": 1987, "месяц": 9, "день": 14,
         "отдел": "ИТ", "должность": "Тестировщик", "оклад": 65000, "стаж": 9},
        {"фамилия": "Алексеев", "имя": "Алексей", "отчество": "Алексеевич", "год": 1993, "месяц": 4, "день": 25,
         "отдел": "Отдел продаж", "должность": "Менеджер", "оклад": 70000, "стаж": 4},
        {"фамилия": "Андреева", "имя": "Анна", "отчество": "Андреевна", "год": 1991, "месяц": 12, "день": 3,
         "отдел": "Бухгалтерия", "должность": "Бухгалтер", "оклад": 58000, "стаж": 6},
        {"фамилия": "Дмитриев", "имя": "Дмитрий", "отчество": "Дмитриевич", "год": 1983, "месяц": 6, "день": 18,
         "отдел": "Производство", "должность": "Технолог", "оклад": 82000, "стаж": 12},
        {"фамилия": "Егоров", "имя": "Егор", "отчество": "Егорович", "год": 1994, "месяц": 2, "день": 28, "отдел": "ИТ",
         "должность": "Программист", "оклад": 85000, "стаж": 2},
        {"фамилия": "Федоров", "имя": "Федор", "отчество": "Федорович", "год": 1986, "месяц": 10, "день": 8,
         "отдел": "Производство", "должность": "Мастер", "оклад": 78000, "стаж": 11},
        {"фамилия": "Григорьева", "имя": "Галина", "отчество": "Григорьевна", "год": 1989, "месяц": 7, "день": 17,
         "отдел": "Отдел кадров", "должность": "Директор", "оклад": 120000, "стаж": 10},
        {"фамилия": "Сергеев", "имя": "Сергей", "отчество": "Сергеевич", "год": 1996, "месяц": 8, "день": 9,
         "отдел": "Отдел продаж", "должность": "Стажер", "оклад": 40000, "стаж": 1},
        {"фамилия": "Павлов", "имя": "Павел", "отчество": "Павлович", "год": 1984, "месяц": 11, "день": 23,
         "отдел": "ИТ", "должность": "Системный администратор", "оклад": 72000, "стаж": 13},
        {"фамилия": "Семенов", "имя": "Семен", "отчество": "Семенович", "год": 1997, "месяц": 5, "день": 19,
         "отдел": "Бухгалтерия", "должность": "Помощник бухгалтера", "оклад": 45000, "стаж": 1},
        {"фамилия": "Макаров", "имя": "Максим", "отчество": "Макарович", "год": 1982, "месяц": 3, "день": 31,
         "отдел": "Производство", "должность": "Начальник цеха", "оклад": 110000, "стаж": 14},
        {"фамилия": "Захарова", "имя": "Зарина", "отчество": "Захаровна", "год": 1998, "месяц": 9, "день": 12,
         "отдел": "Отдел продаж", "должность": "Менеджер", "оклад": 68000, "стаж": 0},
        {"фамилия": "Романов", "имя": "Роман", "отчество": "Романович", "год": 1999, "месяц": 1, "день": 7,
         "отдел": "ИТ", "должность": "Веб-разработчик", "оклад": 88000, "стаж": 1},
        {"фамилия": "Владимирова", "имя": "Вероника", "отчество": "Владимировна", "год": 1981, "месяц": 4, "день": 26,
         "отдел": "Отдел кадров", "должность": "Заместитель директора", "оклад": 95000, "стаж": 16},
        {"фамилия": "Борисов", "имя": "Борис", "отчество": "Борисович", "год": 1990, "месяц": 6, "день": 13,
         "отдел": "Производство", "должность": "Инженер", "оклад": 77000, "стаж": 5},
        {"фамилия": "Кириллов", "имя": "Кирилл", "отчество": "Кириллович", "год": 1988, "месяц": 2, "день": 14,
         "отдел": "ИТ", "должность": "Программист", "оклад": 92000, "стаж": 8},
        {"фамилия": "Тимофеев", "имя": "Тимофей", "отчество": "Тимофеевич", "год": 1993, "месяц": 10, "день": 21,
         "отдел": "Бухгалтерия", "должность": "Экономист", "оклад": 62000, "стаж": 4},
        {"фамилия": "Назаров", "имя": "Назар", "отчество": "Назарович", "год": 1985, "месяц": 12, "день": 6,
         "отдел": "Отдел продаж", "должность": "Руководитель отдела", "оклад": 105000, "стаж": 10},
        {"фамилия": "Артемьев", "имя": "Артем", "отчество": "Артемьевич", "год": 1991, "месяц": 8, "день": 29,
         "отдел": "ИТ", "должность": "Аналитик", "оклад": 87000, "стаж": 6}
    ]

    while True:
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

        choice = input("Выберите действие (1-8): ").strip()

        if choice == "1":
            show_all(employees)
        elif choice == "2":
            employees = add_emp(employees)
        elif choice == "3":
            employees = delete_emp(employees)
        elif choice == "4":
            employees = edit_emp(employees)
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


def show_all(employees):
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


def is_russian_text(text):
    """Проверка, что текст содержит только русские буквы, пробелы и дефисы"""
    for char in text:
        # Русские буквы (строчные и заглавные), пробел, дефис
        if not ('а' <= char <= 'я' or 'А' <= char <= 'Я' or char == ' ' or char == '-' or char == 'ё' or char == 'Ё'):
            return False
    return True


def get_input(prompt, validation=None, error_msg=""):
    """Получить ввод с проверкой"""
    while True:
        value = input(prompt).strip()
        if not value:
            print("Поле не может быть пустым!")
            continue
        if validation and not validation(value):
            if error_msg:
                print(error_msg)
            continue
        return value


def validate_name(name):
    """Проверка имени/фамилии/отчества"""
    if not is_russian_text(name):
        print("Должно содержать только русские буквы!")
        return False
    if any(c.isdigit() for c in name):
        print("Не может содержать цифры!")
        return False
    if not name[0].isupper():
        print("Первая буква должна быть заглавной!")
        return False
    return True


def validate_department(department):
    """Проверка отдела"""
    if not is_russian_text(department):
        print("Отдел должен содержать только русские буквы, пробелы и дефисы!")
        return False
    if any(c.isdigit() for c in department):
        print("Отдел не может содержать цифры!")
        return False
    if len(department) < 2:
        print("Название отдела слишком короткое!")
        return False
    return True


def validate_position(position):
    """Проверка должности"""
    if not is_russian_text(position):
        print("Должность должна содержать только русские буквы, пробелы и дефисы!")
        return False
    if any(c.isdigit() for c in position):
        print("Должность не может содержать цифры!")
        return False
    if len(position) < 2:
        print("Название должности слишком короткое!")
        return False
    return True


def validate_number(value, min_val, max_val, field):
    """Проверка числового значения"""
    try:
        num = int(value)
        if min_val <= num <= max_val:
            return True
        print(f"{field} должен быть от {min_val} до {max_val}!")
        return False
    except:
        print("Ошибка: введите целое число!")
        return False


def validate_salary(value):
    """Проверка оклада"""
    try:
        num = int(value)
        if num > 0:
            return True
        print("Оклад должен быть больше 0!")
        return False
    except:
        print("Ошибка: введите целое число!")
        return False


def validate_day(day_str, year, month):
    """Проверка дня с учетом месяца и года"""
    try:
        day = int(day_str)
        if day < 1 or day > 31:
            print("День должен быть от 1 до 31!")
            return False

        # Дни в месяцах
        days_in_month = [31, 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28,
                         31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if day <= days_in_month[month - 1]:
            return True
        print(f"В этом месяце максимум {days_in_month[month - 1]} дней!")
        return False
    except:
        print("Ошибка: введите целое число!")
        return False


def add_emp(employees):
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


def delete_emp(employees):
    """Удалить сотрудника"""
    if not employees:
        print("Список пуст!")
        return employees

    show_all(employees)

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


def edit_emp(employees):
    """Изменить данные сотрудника"""
    if not employees:
        print("Список пуст!")
        return employees

    show_all(employees)

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


def merge_sort(arr, compare_func):
    """Сортировка слиянием"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], compare_func)
    right = merge_sort(arr[mid:], compare_func)

    # Слияние
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if compare_func(left[i], right[j]) <= 0:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def report1(employees):
    """Отчет 1: сортировка по году, стажу, фамилии"""
    if not employees:
        print("Список пуст!")
        return

    def compare(a, b):
        if a['год'] != b['год']:
            return -1 if a['год'] > b['год'] else 1
        if a['стаж'] != b['стаж']:
            return -1 if a['стаж'] < b['стаж'] else 1
        return -1 if a['фамилия'] < b['фамилия'] else 1

    sorted_emp = merge_sort(employees, compare)

    print("\n" + "=" * 100)
    print("ОТЧЕТ 1: по году (убыв.), стажу (убыв.), фамилии (возр.)")
    print("=" * 100)
    print(f"{'№':3} | {'ФИО':30} | {'Дата рождения':15} | {'Отдел':15} | {'Должность':20} | {'Оклад':10} | {'Стаж':5}")
    print("-" * 100)

    for i, emp in enumerate(sorted_emp, 1):
        date = f"{emp['день']:02d}.{emp['месяц']:02d}.{emp['год']}"
        name = f"{emp['фамилия']} {emp['имя']} {emp['отчество']}"
        print(
            f"{i:3} | {name:30} | {date:15} | {emp['отдел']:15} | {emp['должность']:20} | {emp['оклад']:10} | {emp['стаж']:5}")
    print("=" * 100)


def report2(employees):
    """Отчет 2: сотрудники отдела, сортировка по окладу, фамилии"""
    if not employees:
        print("Список пуст!")
        return

    # Получаем список отделов
    departments = list(set(emp['отдел'] for emp in employees))
    print("\nОтделы:")
    for i, dept in enumerate(departments, 1):
        print(f"{i}. {dept}")

    # Выбор отдела с проверкой
    while True:
        choice = input("\nВыберите отдел (номер): ").strip()

        if not choice:
            print("Ошибка: поле не может быть пустым!")
            continue

        if not choice.isdigit():
            print("Ошибка: введите число!")
            continue

        choice_num = int(choice)
        if choice_num < 1 or choice_num > len(departments):
            print(f"Ошибка: введите число от 1 до {len(departments)}!")
            continue

        dept = departments[choice_num - 1]
        break

    # Фильтруем сотрудников отдела
    dept_emp = [emp for emp in employees if emp['отдел'] == dept]

    if not dept_emp:
        print(f"В отделе '{dept}' нет сотрудников!")
        return

    # Сортируем
    def compare(a, b):
        if a['оклад'] != b['оклад']:
            return -1 if a['оклад'] > b['оклад'] else 1
        return -1 if a['фамилия'] < b['фамилия'] else 1

    sorted_emp = merge_sort(dept_emp, compare)

    print(f"\n" + "=" * 100)
    print(f"ОТЧЕТ 2: отдел '{dept}', оклад (убыв.), фамилия (возр.)")
    print("=" * 100)
    print(f"{'№':3} | {'ФИО':30} | {'Дата рождения':15} | {'Должность':20} | {'Оклад':10} | {'Стаж':5}")
    print("-" * 100)

    for i, emp in enumerate(sorted_emp, 1):
        date = f"{emp['день']:02d}.{emp['месяц']:02d}.{emp['год']}"
        name = f"{emp['фамилия']} {emp['имя']} {emp['отчество']}"
        print(f"{i:3} | {name:30} | {date:15} | {emp['должность']:20} | {emp['оклад']:10} | {emp['стаж']:5}")
    print("=" * 100)


def report3(employees):
    """Отчет 3: сотрудники с окладом выше среднего"""
    if not employees:
        print("Список пуст!")
        return

    # Средний оклад
    avg = sum(emp['оклад'] for emp in employees) / len(employees)

    # Сотрудники с окладом выше среднего
    high_salary = [emp for emp in employees if emp['оклад'] > avg]

    if not high_salary:
        print(f"Нет сотрудников с окладом выше {avg:.2f} руб.!")
        return

    # Сортируем
    def compare(a, b):
        if a['должность'] != b['должность']:
            return -1 if a['должность'] < b['должность'] else 1
        return -1 if a['фамилия'] < b['фамилия'] else 1

    sorted_emp = merge_sort(high_salary, compare)

    print("\n" + "=" * 100)
    print(f"ОТЧЕТ 3: оклад выше среднего ({avg:.2f} руб.)")
    print("Сортировка: должность (возр.), фамилия (возр.)")
    print("=" * 100)
    print(f"{'№':3} | {'ФИО':30} | {'Дата рождения':15} | {'Отдел':15} | {'Должность':20} | {'Оклад':10} | {'Стаж':5}")
    print("-" * 100)

    for i, emp in enumerate(sorted_emp, 1):
        date = f"{emp['день']:02d}.{emp['месяц']:02d}.{emp['год']}"
        name = f"{emp['фамилия']} {emp['имя']} {emp['отчество']}"
        print(
            f"{i:3} | {name:30} | {date:15} | {emp['отдел']:15} | {emp['должность']:20} | {emp['оклад']:10} | {emp['стаж']:5}")
    print("=" * 100)


# Запуск программы
if __name__ == "__main__":
    main()