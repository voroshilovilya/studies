"""
    На вход программе подается последовательность целых чисел от 1 до 5, характеризующее 
    оценку ученика, каждое число на отдельной строке. Концом последовательности является 
    любое неположительное число либо число, большее 55. 
    Напишите программу, которая выводит количество пятерок.

    Формат входных данных
    На вход программе подается последовательность чисел, каждое число на отдельной строке.

    Формат выходных данных
    Программа должна вывести количество пятерок.

    Примечание. 
    Не забываем, что неположительными числами являются все отрицательные числа и число 0.

    Sample Input 1:
    1
    1
    2
    2
    3
    4
    4
    5
    5
    5
    5
    -17
    1
    2
    5
    4
    Sample Output 1:
    4
"""
a = 0
b = 0
while a >= 0 and a<6 :    
    a = int(input())
    if a >= 0 and a<6 and a==5: b+=1
print(b)