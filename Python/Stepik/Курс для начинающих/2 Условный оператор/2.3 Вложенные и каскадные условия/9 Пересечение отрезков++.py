"""
    На числовой прямой даны два отрезка: [𝑎1;𝑏1] и [𝑎2; 𝑏2]. 
    Напишите программу, которая находит их пересечение.

    Пересечением двух отрезков может быть: отрезок, точка, пустое множество:

    Формат входных данных
    На вход программе подаются четыре целых числа 𝑎1,𝑏1,𝑎2,𝑏2​ , 
    каждое на отдельной строке. Гарантируется, что 𝑎1<𝑏1 и 𝑎2<𝑏2​.

    Формат выходных данных
    Программа должна вывести на экран границы отрезка, являющегося пересечением, либо общую точку, либо текст «пустое множество».

    Sample Input 1:
    1
    3
    2
    4
    Sample Output 1:
    2 3
"""
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if (a1<a2 and  b1<a2 ) or (a1>b2 and b1>b2) :
    print("пустое множество")
elif (a1==a2 and b1==b2) : print(a1,b1) 
    
elif (a1==a2 and b1<=b2) : print(a1,b1) 
elif (a1==a2 and b1>=b2) : print(a1,b2)
    
elif (b1==b2 and a1>=a2) : print(a1,b1) 
elif (b1==b2 and a1<=a2) : print(a2,b1) 
    
elif b1==a2 : print(b1)
elif b2==a1 : print(a1)
    
elif (a1<a2 and b1>b2) : print(a2,b2) 
elif (a1>a2 and b1<b2) : print(a1,b1) 
elif (a1<a2 and b1<b2) : print(a2,b1) 
elif (a1>a2 and b1>b2) : print(a1,b2)  
