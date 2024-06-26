"""
    Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.

    Формат входных данных
    На вход программе в первой строке подается число 𝑛 – общее количество слов. Далее идут 𝑛 строк со словами.

    Формат выходных данных
    Программа должна вывести одно число – общее количество уникальных символов во всех словах без учета регистра.

    Sample Input 1:
    5
    aAa
    bB
    ccc
    dDdd
    ppppP
    Sample Output 1:
    5
"""
a = [input().lower() for i in range(int(input()))]
a = ''.join(a)
print(len(set(a)))