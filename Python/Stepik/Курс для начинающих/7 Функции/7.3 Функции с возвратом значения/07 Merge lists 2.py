"""
    На вход программе подается число 𝑛, а затем 𝑛 строк, содержащих целые числа в 
    порядке возрастания. Из данных строк формируются списки чисел. Напишите программу, 
    которая объединяет указанные списки в один отсортированный список с помощью функции 
    quick_merge(), а затем выводит его.

    Формат входных данных
    На вход программе подается натуральное число 𝑛, а затем 𝑛 строк, содержащих целые 
    числа в порядке возрастания, разделенные символом пробела.

    Формат выходных данных
    Программа должна вывести элементы окончательного отсортированного списка каждое через пробел.

    Sample Input 1:
    3
    1 2 3 4
    5 6 7
    10 11 17
    Sample Output 1:
    1 2 3 4 5 6 7 10 11 17
"""
def merge(list1):
    list3 = [int(el) for f in f for el in f]
    return sorted(list3)

# считываем данные
n = int(input())
f = [input().split() for c in range(n)]

# вызываем функцию
print(*merge(f))