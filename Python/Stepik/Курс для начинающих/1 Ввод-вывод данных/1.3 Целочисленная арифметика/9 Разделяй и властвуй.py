"""
    Напишите программу, которая считывает целое положительное число x и выводит на экран последовательность чисел 
    x,2x,3x,4x и 5x, разделённых тремя черточками.

    Формат входных данных
    На вход программе подаётся целое положительное число.

    Формат выходных данных
    Программа должна вывести текст согласно условию задачи.

    Sample Input 1:
    7
    Sample Output 1:
    7---14---21---28---35
"""
a= int(input())
print(a, 2*a, 3*a, 4*a, 5*a, sep="---")