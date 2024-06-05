"""
    Дано пятизначное или шестизначное натуральное число. Напишите программу, 
    которая изменит порядок его последних пяти цифр на обратный.

    Формат входных данных
    На вход программе подается одно натуральное пятизначное или шестизначное число.

    Формат выходных данных
    Программа должна вывести число, которое получится в результате разворота, 
    указанного в условии задачи. Число нужно выводить без незначащих нулей.

    Sample Input 1:
    12345
    Sample Output 1:
    54321
"""
n = input()

print(int(n[:-5] + n[:-6:-1]))