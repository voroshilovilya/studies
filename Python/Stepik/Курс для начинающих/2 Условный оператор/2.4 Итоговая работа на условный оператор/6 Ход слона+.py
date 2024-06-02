"""
    Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли слон 
    попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 
    каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
    Программа должна вывести «YES», если из первой клетки ходом слона можно попасть во вторую или «NO» 
    в противном случае.

    Формат входных данных
    На вход программе подаётся четыре числа от 1 до 8.

    Формат выходных данных
    Программа должна вывести текст в соответствии с условием задачи.

    Примечание. Шахматный слон ходит по диагоналям.

    Sample Input 1:
    4
    4
    5
    5
    Sample Output 1:
    YES
"""
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if (a1+b1==a2+b2) or (a1-b1==a2-b2) : print("YES")
else : print("NO")