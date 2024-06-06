"""
    Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

    Формат входных данных
    На вход программе подаётся натуральное число 𝑛 — количество строк и столбцов в матрице, 
    затем элементы матрицы (целые числа) построчно через пробел.

    Формат выходных данных
    Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

    Примечание. Элементы главной диагонали также учитываются.

    Sample Input 1:
    3
    1 4 5
    6 7 8
    1 1 6
    Sample Output 1:
    7
"""
dimension = int(input())
n = [input().split() for _ in range (dimension)]
print (max([int(n[i][j]) for i in range(len(n)) for j in range(len(n)) if (i >= j and i <= dimension - 1 - j) or (i >= j and i >= dimension - 1 - j) ]) )