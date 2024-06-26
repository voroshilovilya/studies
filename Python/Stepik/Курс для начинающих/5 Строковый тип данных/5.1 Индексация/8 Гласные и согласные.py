"""
    На вход программе подается одна строка с буквами русского языка. Напишите программу, 
    которая определяет количество гласных и согласных звуков.

    Формат входных данных
    На вход программе подается одна строка.

    Формат выходных данных
    Программа должна вывести количество гласных и согласных звуков.

    Примечание. В русском языке 9 букв, передающих гласные звуки, и 21 буква, 
    передающая согласные звуки (букву ё игнорируем):
    ауоыиэяюе
    бвгджзйклмнпрстфхцчшщ

    Sample Input:
    Вдохновение – это умение приводить себя в рабочее состояние!
    Sample Output:
    Количество гласных букв равно 25
    Количество согласных букв равно 24
"""
s = 0
s1 = 0
n = input()
for i in range (len(n)):
    if n[i] in "ауоыиэяюёеАУОЫИЭЯЮЁЕ": s +=1
    if n[i] in "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ": s1 +=1

print(f"Количество гласных букв равно {s}")
print(f"Количество согласных букв равно {s1}")