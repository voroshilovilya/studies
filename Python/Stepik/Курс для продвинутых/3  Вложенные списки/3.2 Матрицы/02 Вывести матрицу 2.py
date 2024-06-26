"""
    На вход программе подаются два натуральных числа 𝑛 и 𝑚, каждое на отдельной строке — количество строк и 
    столбцов в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд 
    идут элементы сначала первой строки, затем второй, и т.д.
    
    Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы, 
    выводит пустую строку, и снова ту же матрицу, но уже поменяв местами строки со столбцами: первая 
    строка выводится как первый столбец, и так далее.
    
    Формат входных данных
    На вход программе подаются два числа 𝑛 и 𝑚 — количество строк и столбцов в матрице, далее идут 𝑛×𝑚 слов, 
    каждое на отдельной строке.
    
    Формат выходных данных
    Программа должна вывести считанную матрицу, за ней пустую строку и ту же матрицу, но поменяв местами строки со столбцами. 
    Элементы матрицы разделять одним пробелом.
    
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
    
    и и и дуде
    швец жнец на игрец
"""
y,x = int(input()), int(input())
n = [ [input() for i in range(x)] for j in range (y)]
[print(*row) for row in n]
print()
for i in range(x):
    for j in range(y):
        print(n[j][i], end=" ")
    print()