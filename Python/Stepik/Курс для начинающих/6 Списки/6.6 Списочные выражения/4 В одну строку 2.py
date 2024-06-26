"""
    На вход программе подается строка текста. Напишите программу, использующую списочное выражение, 
    которая выводит все цифровые символы данной строки.

    Формат входных данных
    На вход программе подается строка текста.

    Формат выходных данных
    Программа должна вывести текст в соответствии с условием задачи.

    Примечание. Программу можно написать в одну строку кода.

    Sample Input 1:
    Число Pi примерно равно 3.1415
    Sample Output 1:
    31415
"""
n = [c for c in input() if c in '0123456789']
print(*n, sep="")