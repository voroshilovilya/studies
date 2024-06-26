"""
    Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, 
    стоящие на главной и побочной диагонали, при этом каждый элемент должен остаться в 
    том же столбце (то есть в каждом столбце нужно поменять местами элемент на главной 
    диагонали и на побочной диагонали).

    Формат входных данных
    На вход программе подаётся натуральное число 𝑛 — количество строк и столбцов в матрице, 
    затем элементы матрицы построчно через пробел.

    Формат выходных данных
    Программа должна вывести матрицу с элементами главной и побочной диагонали, поменявшимися 
    своими местами.

    Sample Input 1:
    3
    1 2 3
    4 5 6
    7 8 9
    Sample Output 1:
    7 2 9 
    4 5 6 
    1 8 3 
"""
x = int(input())
n = [input().split() for _ in range(x) ]
for i in range(x):
    for j in range(x):
        if i == j :
            n[i][j], n[x-1-j][i] = n[x-1-j][i], n[i][j]

[print(*i) for i in n]