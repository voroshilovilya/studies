"""
    Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

    Формат входных данных
    На вход программе подаются 10 целых чисел, каждое на отдельной строке.

    Формат выходных данных
    Программа должна вывести произведение отличных от нуля чисел.

    Примечание 1. Гарантируется, что хотя бы одно из 10 чисел является ненулевым.

    Примечание 2. Отличные от нуля числа – те числа, которые не равны нулю.

    Sample Input 1:
    8
    0
    1
    2
    1
    0
    0
    5
    4
    12
    Sample Output 1:
    3840
"""
s = 1
for i in range (10):
    n = int(input())
    if n!=0 :
        s*=n
print(s)