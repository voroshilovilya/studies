"""
    На вход программе подается последовательность слов, каждое слово на отдельной строке. 
    Концом последовательности является слово «КОНЕЦ» (без кавычек). При этом само слово «КОНЕЦ» 
    не входит в последовательность, лишь символизируя её окончание. Напишите программу, 
    которая выводит члены данной последовательности.

    Формат входных данных
    На вход программе подается последовательность слов, каждое слово на отдельной строке.

    Формат выходных данных
    Программа должна вывести члены данной последовательности.

    Sample Input 1:
    Fus
    Ro
    КОНЕЦ
    Dah
    Sample Output 1:
    Fus
    Ro
"""
a = ""

while a != "КОНЕЦ":    
    a = input()
    if a != "КОНЕЦ":print (a)