"""
    апишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам.

    Формат входных данных
    На вход программе подаётся целое число x.

    Формат выходных данных
    Программа должна вывести текст в соответствии с условием задачи.

    Примечание. Если точка выколотая, то граница не включается, если точка закрашенная, то граница включается. 

    Sample Input 1:
    -44
    Sample Output 1:
    Принадлежит
"""
a1= int(input())
if a1<=-3 or a1>=7 :
    print("Принадлежит")
else:
    print("Не принадлежит")