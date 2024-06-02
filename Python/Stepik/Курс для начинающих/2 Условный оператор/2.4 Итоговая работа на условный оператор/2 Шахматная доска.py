"""
    Заданы две клетки шахматной доски. Напишите программу, которая определяет, имеют ли указанные клетки один цвет или нет. 
    Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета, то «NO».

    На вход программе подаётся четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

    Формат выходных данных
    Программа должна вывести текст в соответствии с условием задачи.

    Sample Input 1:
    1
    1
    2
    6
    Sample Output 1:
    YES
"""
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if ((a1%2==1 and b1%2==1) or (a1%2==0 and b1%2==0)) and ((a2%2==1 and b2%2==1) or (a2%2==0 and b2%2==0)) : print("YES")
    
elif((a1%2==1 or b1%2==1) and (a1%2==0 or b1%2==0)) and ((a2%2==1 or b2%2==1) and (a2%2==0 or b2%2==0)) : print("YES")
     
else : print("NO")