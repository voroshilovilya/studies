"""
    Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли конь попасть 
    с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие 
    номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести 
    «YES», если из первой клетки ходом коня можно попасть во вторую или «NO» в противном случае.

    Формат входных данных
    На вход программе подаётся четыре числа от 1 до 8.

    Формат выходных данных
    Программа должна вывести текст в соответствии с условием задачи.

    Примечание. Шахматный конь ходит буквой «Г».

    Sample Input 1:
    1
    1
    8
    8
    Sample Output 1:
    NO
"""
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if (abs(a1-a2) == 1 and abs(b1-b2) == 2 ) or (abs(a1 - a2) == 2 and abs(b1 - b2) == 1) : print("YES")
else : print("NO")