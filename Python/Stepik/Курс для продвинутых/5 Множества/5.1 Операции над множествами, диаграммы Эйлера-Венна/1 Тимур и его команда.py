"""
    На летних каникулах Тимур и ученики онлайн-школы BEEGEEK решили отдохнуть. В результате 𝑛 учеников 
    школы поехали отдыхать на море, 𝑚 учеников съездили в деревню, а 𝑘 учеников сходили в горы. Оказалось, 
    что и в деревне, и на море были 𝑥 учеников, а в деревне и в горах — 𝑦 учеников. Побывать и в горах, 
    и на море не удалось никому. 

    Напишите программу для определения количества учеников в школе, если никто не смог посетить все три 
    места сразу, а 𝑧 учеников писали ДВИ по математике для поступления в МГУ, и никуда не ездили.

    Формат входных данных
    На вход программе подаются числа 𝑛,𝑚,𝑘,𝑥,𝑦,𝑧, каждое на отдельной строке.

    Формат выходных данных
    Программа должна вывести одно число в соответствии с условием задачи.

    Примечание. 
    𝑛 – все ученики, которые поехали на море, 
    𝑚 – все ученики, которые съездили в деревню, и 
    𝑘 – все ученики, которые сходили в горы.

    Sample Input:
    14
    16
    5
    10
    3
    2
    Sample Output:
    24
"""
n, m, k, x, y, z = [int(input()) for i in range(6)]

a = (n-x)+m+(k-y)+z

print(a)