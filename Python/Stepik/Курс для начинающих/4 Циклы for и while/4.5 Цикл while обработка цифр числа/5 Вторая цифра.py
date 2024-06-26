"""
    Дано натуральное число 𝑛(𝑛>9). Напишите программу, которая определяет его вторую (с начала) цифру.

    Формат входных данных 
    На вход программе подается одно натуральное число, состоящее как минимум из двух цифр.

    Формат выходных данных
    Программа должна вывести его вторую (с начала) цифру.

    Sample Input 1:
    455672
    Sample Output 1:
    5
"""
a = int(input())

while a > 99:
    a //=10

print(a%10)