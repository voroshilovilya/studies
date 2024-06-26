"""
    Напишите программу, вычисляющую значение тригонометрического выражения 
    sinx+cosx+tan**2 x по заданному числу градусов 𝑥.
    
    Формат входных данных
    На вход программе подается одно вещественное число 𝑥 измеряемое в градусах​. 
    
    Формат выходных данных
    Программа должна вывести одно число – значение тригонометрического выражения.
    
    Примечание 1. Тригонометрические функции принимают аргумент в радианах. 
    Чтобы перевести градусы в радианы, воспользуйтесь формулой 𝑟=𝑥⋅𝜋/180
    
    Примечание 2. Модуль math содержит встроенную функцию radians(), которая переводит угол из градусов в угол в радианах.
    
    Sample Input 1:
    30.0
    Sample Output 1:
    1.6993587371177719
"""
from math import radians, sin, cos, tan
a1 = float(input())

print( sin(radians(a1))+cos(radians(a1))+tan(radians(a1))**2 )