"""
    Напишите программу для вычисления суммы двух матриц.

    Формат входных данных
    На вход программе подаются два натуральных числа 𝑛 и 𝑚 — количество строк и столбцов в матрицах, 
    затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.

    Формат выходных данных
    Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

    Sample Input 1:
    2 4
    1 2 3 4
    5 6 7 1

    3 2 1 2
    1 3 1 3
    Sample Output 1:
    4 4 4 6
    6 9 8 4
"""
n,m = [ int(i) for i in input().split()]
a = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    a.append(temp)
c = input()
b = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    b.append(temp)
for i in range(n):
    for j in range(m):
        a[i][j] = a[i][j] + b[i][j]    
[print(*i) for i in a]