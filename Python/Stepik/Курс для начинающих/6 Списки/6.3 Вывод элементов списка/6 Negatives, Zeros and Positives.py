"""
    На вход программе подается натуральное число 𝑛, а затем 𝑛 целых чисел. 
    Напишите программу, которая сначала выводит все отрицательные числа, 
    затем нули, а затем все положительные числа, каждое на отдельной строке. 
    Числа должны быть выведены в том же порядке, в котором они были введены.

    Формат входных данных
    На вход программе подаются натуральное число 𝑛, а затем 𝑛 целых чисел, 
    каждое на отдельной строке.

    Формат выходных данных
    Программа должна вывести текст в соответствии с условием задачи.

    Sample Input 1:
    7
    3
    -4
    1
    0
    -1
    0
    -2
    Sample Output 1:
    -4
    -1
    -2
    0
    0
    3
    1
"""
a, b, c = [],[],[]

for i in range(int(input())):
    t = int(input())
    if t > 0 : a.append(t)
    elif t==0 : b.append(t)
    elif t<0 : c.append(t)

        
print(*c, *b, *a, sep="\n")
