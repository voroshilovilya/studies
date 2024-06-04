"""
    На вход программе подается натуральное число 𝑛, затем 𝑛 строк, затем 
    число 𝑘 — количество поисковых запросов, затем 𝑘 строк — поисковые запросы. 
    Напишите программу, которая выводит все введенные строки, в которых 
    встречаются одновременно все поисковые запросы.

    Формат входных данных
    На вход программе подаются натуральное число 𝑛 — количество строк, затем 
    сами строки в указанном количестве, затем число 𝑘, затем сами поисковые запросы.

    Формат выходных данных
    Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.

    Примечание. Поиск не должен быть чувствителен к регистру символов.

    Sample Input:
    5
    Язык Python прекрасен
    C# - отличный язык программирования
    Stepik - отличная платформа
    BEEGEEK FOREVER!
    язык Python появился 20 февраля 1991
    2
    язык
    python
    Sample Output:
    Язык Python прекрасен
    язык Python появился 20 февраля 1991
"""
a = [input() for _ in range(int(input()))]
b = [input() for _ in range(int(input()))]
count=0
c = []
for i in a:
    count = 0
    for j in b:
        
        if j.lower() in i.lower():
            count+=1
        if count == len(b):
            c.append(i)
            
print(*c, sep="\n")