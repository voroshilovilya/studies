"""
    На вход программе подается число n – количество собачьих лет. Напишите программу, 
    которая вычисляет возраст собаки в человеческих годах по следующему алгоритму: 
    в течение первых двух лет собачий год равен 10.5 человеческим годам, 
    после этого каждый год собаки равен 4 человеческим годам.

    Формат входных данных
    На вход программе подаётся натуральное число – количество собачьих лет.

    Формат выходных данных
    Программа должна вывести возраст собаки в человеческих годах.

    Sample Input 1:
    1
    Sample Output 1:
    10.5
"""
a1 = float(input())
if a1<=2 : print(a1*10.5)
else : print(21+(a1-2)*4)