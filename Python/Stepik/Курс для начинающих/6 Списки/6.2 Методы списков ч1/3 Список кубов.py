"""
    На вход программе подается натуральное число 𝑛, а затем 𝑛 целых чисел. 
    Напишите программу, которая создает из указанных чисел список их кубов.

    Формат входных данных
    На вход программе подаются натуральное число 𝑛, а затем 𝑛 целых чисел, каждое на отдельной строке.

    Формат выходных данных
    Программа должна вывести список, состоящий из кубов указанных чисел.

    Sample Input 1:
    5
    1
    2
    3
    4
    5
    Sample Output 1:
    [1, 8, 27, 64, 125]
"""
a = list()

for i in range (int(input())):
    a.append(int(input()))
    a[i]**=3
    
print (a)