"""
Модуль для формирования отчетов и сортировки
"""


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
    show_employees_table(sorted_emp)


def report2(employees):
    """Отчет 2: сотрудники отдела, сортировка по окладу, фамилии"""
    from database import get_departments

    if not employees:
        print("Список пуст!")
        return

    # Получаем список отделов
    departments = get_departments(employees)
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
    from database import get_average_salary

    if not employees:
        print("Список пуст!")
        return

    # Средний оклад
    avg = get_average_salary(employees)

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
    show_employees_table(sorted_emp)


def show_employees_table(employees):
    """Показать таблицу сотрудников"""
    print(f"{'№':3} | {'ФИО':30} | {'Дата рождения':15} | {'Отдел':15} | {'Должность':20} | {'Оклад':10} | {'Стаж':5}")
    print("-" * 100)

    for i, emp in enumerate(employees, 1):
        date = f"{emp['день']:02d}.{emp['месяц']:02d}.{emp['год']}"
        name = f"{emp['фамилия']} {emp['имя']} {emp['отчество']}"
        print(
            f"{i:3} | {name:30} | {date:15} | {emp['отдел']:15} | {emp['должность']:20} | {emp['оклад']:10} | {emp['стаж']:5}")
    print("=" * 100)