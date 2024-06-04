"""
    Дано натуральное число. Напишите программу, которая определяет, является ли 
    последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.

    Формат входных данных 
    На вход программе подается одно натуральное число.

    Формат выходных данных
    Программа должна вывести «YES», если последовательность его цифр при просмотре справа 
    налево является упорядоченной по неубыванию, или «NO» в противном случае.

    Sample Input 1:
    5321
    Sample Output 1:
    YES
"""
a= int(input())
b = int()
c = True
while a !=0:
    if b>a%10 : c = False
    b=a%10
    a//=10
if c==1 : print("YES")
else : print("NO")