"""
    Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:

    Hello <введённое имя> <введённая фамилия>! You have just delved into Python
    Формат входных данных
    На вход программе подаются две строки (имя и фамилия), каждая на отдельной строке.

    Формат выходных данных
    Программа должна вывести текст в соответствии с условием задачи.

    Sample Input 1:
    Anthony
    Joshua
    Sample Output 1:
    Hello Anthony Joshua! You have just delved into Python
"""
a1, b1 = input(), input()
print(f"Hello {a1} {b1}! You just delved into Python")