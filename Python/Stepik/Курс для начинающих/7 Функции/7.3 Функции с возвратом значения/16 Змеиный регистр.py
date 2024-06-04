"""
    Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента 
    строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

    Примечание 1. Почитать подробнее о стилях именования можно тут.

    Примечание 2. Следующий программный код:
    print(convert_to_python_case('ThisIsCamelCased'))
    print(convert_to_python_case('IsPrimeNumber'))

    должен выводить:
    this_is_camel_cased
    is_prime_number

    Sample Input:
    ThisIsCamelCased
    Sample Output:
    this_is_camel_cased
"""
def convert_to_python_case(text):
    res = text[0].lower()
    for i in range(1, len(text)):
        if text[i] == text[i].lower(): res = res + text[i]
        else : res = res + "_" + text[i].lower()
    return res

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))