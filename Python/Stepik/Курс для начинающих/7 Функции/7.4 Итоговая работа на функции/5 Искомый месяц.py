"""
    Напишите функцию get_month(language, number), которая принимает на вход два 
    аргумента language – язык ru или en и number – номер месяца (от 1 до 12) и 
    возвращает название месяца на русском или английском языке.

    Примечание. Следующий программный код:
    print(get_month('ru', 1))
    print(get_month('ru', 12))
    print(get_month('en', 1))
    print(get_month('en', 10))

    должен выводить:
    январь
    декабрь
    january
    october
"""
def get_month(language, number):
    lng_ru = ["", 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    lng_en = ["", 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == "ru": return lng_ru[number]
    else : return lng_en[number]

# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))