"""
    На вход программе подаются два натуральных числа 𝑛 и 𝑚 — количество строк и столбцов в матрице, 
    затем 𝑛 строк по 𝑚 целых чисел в каждой, отделенных символом пробела.

    Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.

    Формат входных данных
    На вход программе на разных строках подаются два числа 𝑛 и 𝑚 — количество строк и столбцов в матрице, 
    затем сами элементы матрицы построчно через пробел.

    Формат выходных данных
    Программа должна вывести два числа: номер строки и номер столбца, в которых стоит наибольший элемент таблицы. 
    Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны 
    то тот, у которого меньше номер столбца.

    Примечание. Считайте, что нумерация строк и столбцов начинается с нуля.

    Sample Input 1:
    3
    4
    0 3 2 4
    2 3 5 5
    5 1 2 3
    Sample Output 1:
    1 2
"""
y, x = int(input()), int(input())
n = [ [int(i) for i in input().split()] for j in range (y)]
i1=0
j1=0
big = (-1)*10**10
for i in range (y):
    for j in range (x): 
        if n[i][j] > big:
            big = n[i][j]
            i1=i
            j1=j
print(i1,j1)