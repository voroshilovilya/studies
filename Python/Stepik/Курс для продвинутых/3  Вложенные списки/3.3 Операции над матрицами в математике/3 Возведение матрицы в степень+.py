"""
    Напишите программу, которая возводит квадратную матрицу в 𝑚-ую степень.

    Формат входных данных
    На вход программе подаётся натуральное число 𝑛 — количество строк и столбцов в матрице, 
    затем элементы матрицы, затем натуральное число 𝑚.

    Формат выходных данных
    Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

    Sample Input 1:
    3
    1 2 3
    4 5 6
    7 8 9
    2
    Sample Output 1:
    30 36 42
    66 81 96
    102 126 150
"""
def stepen (mat1, mat2, x):
    c = [[0] * x for _ in range(x)]
    for i in range(x):
        for j in range(x):
            for q in range(x):
                c[i][j] += mat1[i][q] * mat2[q][j]
    return c                                       


n = int(input())
a = [[int(i) for i in input().split()] for _ in range(n)]
st = int(input())

b = a.copy()

for i in range(st-1):
    b = stepen (a,b,n)
    
[print(*i) for i in b]