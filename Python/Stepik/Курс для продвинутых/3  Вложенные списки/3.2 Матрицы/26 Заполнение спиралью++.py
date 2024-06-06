"""
    На вход программе подаются два натуральных числа 𝑛 и 𝑚. Напишите программу, которая создает матрицу 
    размером 𝑛×𝑚, заполнив её "спиралью" в соответствии с образцом.

    Формат входных данных
    На вход программе на одной строке подаются два натуральных числа 𝑛 и 𝑚 — количество строк и столбцов 
    в матрице.

    Формат выходных данных
    Программа должна вывести матрицу в соответствии образцом.

    Примечание. Для вывода элементов матрицы как в примерах отводите ровно 3 символа на каждый элемент. 
    Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 

    Sample Input 1:
    4 5
    Sample Output 1:
    1  2  3  4  5
    14 15 16 17 6
    13 20 19 18 7
    12 11 10 9  8
"""
r, c  = [ int(i) for i in input().split()]
x, s = r, c
a = [[0 for i in range(c)] for j in range(r)] 
count = 0 
qwe = r*c
for i in range(c):   
    count += 1
    a[0][i] = count
j = 0   # указываем последнюю заполненную ячейку
i = 0
i = c-1
r -= 1
c -= 1
while qwe != count:  
    for k in range(r):  #движение вниз
        j += 1
        count += 1
        a[j][i] = count        
    if qwe == count:
        break
    for k in range(c):  #движение влево
        i -= 1
        count += 1 
        a[j][i] = count
    if qwe == count:
        break
    r -= 1    
    for k in range(r):  #движение вверх
        j -= 1
        count += 1
        a[j][i] = count
    if qwe == count:
        break
    c -= 1   
    for k in range(c): #движение вправо
        i += 1
        count += 1
        a[j][i] = count
    r -= 1
    c -= 1

for i in range(x):
    for j in range(s):
        print(str(a[i][j]).ljust(3), end=' ')
    print()