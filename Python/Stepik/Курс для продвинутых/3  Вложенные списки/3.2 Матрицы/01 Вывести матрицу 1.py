"""
    На вход программе подаются два натуральных числа 𝑛 и 𝑚, каждое на отдельной строке — количество 
    строк и столбцов в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной 
    строке; подряд идут элементы сначала первой строки, затем второй, и т.д.

    Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.

    Формат входных данных
    На вход программе подаются два числа 𝑛 и 𝑚 — количество строк и столбцов в матрице, далее идут 𝑛×𝑚 слов, 
    каждое на отдельной строке.

    Формат выходных данных
    Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.

    Sample Input 1:
    4
    2
    и
    швец
    и
    жнец
    и
    на
    дуде
    игрец
    Sample Output 1:
    и швец
    и жнец
    и на
    дуде игрец
"""
x, y = int(input()), int(input())
n = [[input() for i in range (y)] for j in range(x)]
[print(*row) for row in n]