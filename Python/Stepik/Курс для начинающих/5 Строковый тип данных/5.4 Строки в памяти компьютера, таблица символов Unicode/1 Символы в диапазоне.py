"""
    На вход программе подаются два числа 𝑎 и 𝑏. Напишите программу, которая для 
    каждого кодового значения в диапазоне от 𝑎 до 𝑏 (включительно), выводит 
    соответствующий ему символ из таблицы символов Unicode.

    Формат входных данных 
    На вход программе подается два натуральных числа, каждое на отдельное строке.

    Формат выходных данных
    Программа должна вывести текст в соответствии с условием задачи.

    Sample Input 1:
    65
    70
    Sample Output 1:
    A B C D E F
"""
a, b = int(input()), int(input())

for i in range (a, b+1):
    print(chr(i), end=" ")