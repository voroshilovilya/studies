"""
    Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. 
    Если число находится вне диапазона 1 − 10, то программа должна вывести текст «ошибка».

    В таблице приведены римские цифры для чисел от 1 до 10.
    Число	Римская цифра
    1	        I
    2	        II
    3	        III
    4       	IV
    5       	V
    6	        VI
    7       	VII
    8	        VIII
    9	        IX
    10	        X

    Формат входных данных
    На вход программе подаётся целое число.

    Формат выходных данных
    Программа должна вывести текст в соответствии с условием задачи.

    Sample Input 1:
    7
    Sample Output 1:
    VII
"""
a1= int(input())

if ( a1<1 or a1>10 ) : print("ошибка") 
elif a1<=3 : print(a1%5*"I")
elif a1==4 : print("IV")
elif 4<=a1<=8 : print("V"+a1%5*"I") 
elif a1==9 : print("IX")
else: print("X") 
