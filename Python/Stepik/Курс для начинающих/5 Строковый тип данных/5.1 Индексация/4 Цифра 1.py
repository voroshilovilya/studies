"""
    На вход программе подается одна строка состоящая из цифр. 
    Напишите программу, которая считает сумму цифр данной строки.

    Формат входных данных
    На вход программе подается одна строка состоящая из цифр.

    Формат выходных данных
    Программа должна вывести сумму цифр данной строки.

    Sample Input:
    2514
    Sample Output:
    12
"""
n = input()
s = 0
for i in range(len(n)):
    s+=int(n[i])
print(s)