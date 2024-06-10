"""
    Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.

    Формат входных данных
    На вход программе в первой строке подается число 𝑛 – общее количество слов. Далее идут 𝑛 строк с словами.

    Формат выходных данных
    Программа должна вывести на отдельной строке количество уникальных символов для каждого слова.

    Sample Input 1:
    3
    Тимур
    Beegeek
    АнанАс
    Sample Output 1:
    5
    4
    3
"""
print(*[len(set(input().lower())) for i in range (int(input()))], sep = '\n')