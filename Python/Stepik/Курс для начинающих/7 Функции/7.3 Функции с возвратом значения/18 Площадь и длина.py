"""
    Напишите функцию get_circle(radius), которая принимает в качестве аргумента 
    радиус окружности и возвращает два значения: длину окружности и площадь круга, 
    ограниченного данной окружностью.

    Примечание 1. Длина окружности и площадь круга радиуса 𝑟 вычисляются по формулам:
    С=2𝜋𝑟,𝑆=𝜋𝑟**2. 

    Примечание 2. Для числа 𝜋 используйте глобальную константу из модуля math.

    Примечание 3. Приведенный ниже код:
    print(get_circle(1))
    print(get_circle(1.5))

    должен выводить:
    6.283185307179586 3.141592653589793
    9.42477796076938 7.0685834705770345
"""
from math import pi
def get_circle(radius):
    return 2*radius*pi, pi*radius**2

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)
