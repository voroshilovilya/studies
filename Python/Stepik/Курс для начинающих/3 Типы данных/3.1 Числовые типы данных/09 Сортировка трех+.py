"""
    Напишите программу, которая упорядочивает три числа от большего к меньшему.

    Формат входных данных
    На вход программе подается три целых числа, каждое на отдельной строке.

    Формат выходных данных
    Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.

    Примечание. Учитывайте, что числа могут быть равны.

    Sample Input 1:
    132
    129
    135
    Sample Output 1:
    135
    132
    129
"""
a1, b1, c1 = int(input()), int(input()), int(input())
print(max(a1, b1, c1), a1+b1+c1-max(a1, b1, c1)-min(a1, b1, c1), min(a1, b1, c1), sep="\n")