"""
    Назовём число интересным, если в нём разность максимальной и минимальной цифры равняется 
    средней по величине цифре. Напишите программу, которая определяет, интересное число или нет. 
    Если число интересное, следует вывести «Число интересное», иначе – «Число неинтересное».

    Формат входных данных
    На вход программе подается целое трёхзначное число.

    Формат выходных данных
    Программа должна вывести текст в соответствии с условием задачи.

    Sample Input 1:
    945
    Sample Output 1:
    Число интересное
"""
a1= int(input())
if abs(max(a1%10,a1//100,(a1//10)%10)-min(a1%10,a1//100,(a1//10)%10)) == a1%10+a1//100+(a1//10)%10-max(a1%10,a1//100,(a1//10)%10)-min(a1%10,a1//100,(a1//10)%10) :  print("Число интересное")
else : print("Число неинтересное")