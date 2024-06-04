"""
    На вход программе подается одно слово, записанное в нижнем регистре. 
    Напишите программу, которая определяет, является ли оно палиндромом.

    Формат входных данных
    На вход программе подается одно слово в нижнем регистре.

    Формат выходных данных
    Программа должна вывести «YES», если слово является палиндромом, и «NO» в противном случае.

    Примечание. Палиндром считается слово, которое читается одинаково в обоих направлениях. 
    Например, слово «потоп» является палиндромом.

    Sample Input 1:
    потоп
    Sample Output 1:
    YES
"""
n = input()

if n == n[::-1]: print("YES")
else : print("NO")