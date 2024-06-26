"""
    Даны два целых числа 𝑚 и 𝑛 (𝑚>𝑛). Напишите программу, которая выводит 
    все нечетные целые числа от 𝑚 до 𝑛 включительно в порядке убывания.

    Формат входных данных
    На вход программе подаются два целых числа 𝑚 и 𝑛, каждое на отдельной строке.

    Формат выходных данных
    Программа должна вывести числа в соответствии с условием задачи.

    Примечание. Попробуйте решить задачу двумя способами: с использованием условного оператора if и без него.

    Sample Input 1:
    77
    62
    Sample Output 1:
    77
    75
    73
    71
    69
    67
    65
    63
"""
m, n = int(input()), int(input())
if m%2==1:
    for i in range(m, n, -2) : print(i)
else:
    for i in range(m-1, n-1, -2): print(i)