"""
    Напишите программу, выводящую следующий список:
    ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]

    Формат выходных данных
    Программа должна вывести указанный список.

    Примечание 1. Последний элемент списка должен состоять из 26 символов z.

    Примечание 2. Английский алфавит (для копирования):
    abcdefghijklmnopqrstuvwxyz
"""
a = list()

for i in range (1, 27):
    a.append(chr(96+i)*i)
    
print (a)