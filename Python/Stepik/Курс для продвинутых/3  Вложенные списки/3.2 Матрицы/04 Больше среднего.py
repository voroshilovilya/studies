"""
    Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, 
    больших среднего арифметического элементов данной строки.

    Формат входных данных
    На вход программе подаётся натуральное число 𝑛 — количество строк и столбцов в матрице, 
    затем элементы матрицы (целые числа) построчно через пробел.

    Формат выходных данных
    Программа должна вывести 𝑛 чисел — для каждой строки количество элементов матрицы, 
    больших среднего арифметического элементов данной строки.

    Sample Input 1:
    4
    1 2 3 4
    5 6 3 15
    0 2 3 1
    5 2 8 5
    Sample Output 1:
    2
    1
    2
    1
"""
dimension = int(input())
n = [input().split() for _ in range (dimension)] 
#[print(*i) for i in n]

for i in range(len(n)):
    temp = 0
    count = 0
    for j in range (len(n)):
        temp += int(n[i][j])
    for j in range (len(n)):
        if int(n[i][j]) > temp/len(n): count+=1
    print(count)