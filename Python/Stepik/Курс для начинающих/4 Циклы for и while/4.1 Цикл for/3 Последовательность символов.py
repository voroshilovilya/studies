"""
    Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:
    AAA
    AAA
    AAA
    AAA
    AAA
    AAA
    BBBB
    BBBB
    BBBB
    BBBB
    BBBB
    E
    TTTTT
    TTTTT
    TTTTT
    TTTTT
    TTTTT
    TTTTT
    TTTTT
    TTTTT
    TTTTT
    G
    Формат входных данных
    
    Формат выходных данных
    Программа должна вывести указанную последовательность символов.
    
    Sample Input:
    
    Sample Output:
    AAA
    AAA
    AAA
    AAA
    AAA
    AAA
    BBBB
    BBBB
    BBBB
    BBBB
    BBBB
    E
    TTTTT
    TTTTT
    TTTTT
    TTTTT
    TTTTT
    TTTTT
    TTTTT
    TTTTT
    TTTTT
    G
"""
for i in range (6) : print("A" * 3)
for i in range (5) : print("B" * 4)
print("E")
for i in range (9) : print("T" * 5)
print("G")