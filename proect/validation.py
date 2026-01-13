"""
Модуль для проверки корректности вводимых данных
"""


def is_russian_text(text):
    """Проверка, что текст содержит только русские буквы, пробелы и дефисы"""
    for char in text:
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