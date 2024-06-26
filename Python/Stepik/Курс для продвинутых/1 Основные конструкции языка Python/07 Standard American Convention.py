"""
    На вход программе подаётся натуральное число. Напишите программу, 
    которая вставляет в заданное число запятые в соответствии со 
    стандартным американским соглашением о запятых в больших числах.

    Формат входных данных
    На вход программе подается натуральное число 𝑛 (0<𝑛<10**100)

    Формат выходных данных
    Программа должна вывести число с запятыми в соответствии с условием задачи.

    Sample Input 1:
    1000000
    Sample Output 1:
    1,000,000
"""
n = int(input())
print(f"{n:,}")