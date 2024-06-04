"""
    На вход программе подается натуральное число 𝑛. Напишите программу, которая вычисляет 𝑛!.

    Входные данные
    На вход программе подается натуральное число 𝑛.

    Выходные данные
    Программа должна вывести единственное число в соответствии с условием задачи.

    Примечание. Факториалом натурального числа 𝑛, называется произведение 
    всех натуральных чисел от 1 до 𝑛, то есть 𝑛!=1⋅2⋅3⋅…⋅𝑛

    Sample Input 1:
    3
    Sample Output 1:
    6
"""
n = int(input())
s = 1
for i in range (1, n+1):
    s*=i
print(s)