"""
    Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.

    Формат входных данных 
    На вход программе подается одно натуральное число.

    Формат выходных данных
    Программа должна вывести число, записанное в обратном порядке.

    Sample Input 1:
    5086334
    Sample Output 1:
    4336805
"""
a = int(input())

while a != 0:
    print(a%10, end="")
    a = a // 10