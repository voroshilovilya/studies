"""
    На вход программе подается натуральное число, записанное в десятичной системе счисления. 
    Напишите программу, которая переводит данное число в двоичную систему счисления.

    Формат входных данных
    На вход программе подается одно натуральное число.

    Формат выходных данных
    Программа должна вывести число записанное в двоичной системе счисления.

    Sample Input 1:
    5
    Sample Output 1:
    101
"""
s = ""
s1 = 0
n = int(input())
while n > 0:
    s = s + str(n%2)
    n//=2

print(s[::-1])