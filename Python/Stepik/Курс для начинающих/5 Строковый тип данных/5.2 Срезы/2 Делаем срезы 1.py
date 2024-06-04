"""
    На вход программе подается одна строка. Напишите программу, которая выводит: 
    общее количество символов в строке;
    исходную строку, повторенную 3 раза;
    первый символ строки;
    первые три символа строки;
    последние три символа строки;
    строку в обратном порядке;
    строку с удаленным первым и последним символами.

    Формат входных данных
    На вход программе подается одна строка, длина которой больше 3 символов.

    Формат выходных данных
    Программа должна вывести данные в соответствии с условием. Каждое значение выводится на отдельной строке.

    Sample Input:
    abcdefghijklmnopqrstuvwxyz
    Sample Output:
    26
    abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
    a
    abc
    xyz
    zyxwvutsrqponmlkjihgfedcba
    bcdefghijklmnopqrstuvwxy
"""
n = input()

print(len(n))
print(n*3)
print(n[0])
print(n[:3:])
print(n[-3::])
print(n[::-1])
print(n[1:-1:])