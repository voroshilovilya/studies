"""
    Напишите программу, которая считывает с клавиатуры два целых числа и строку. 
    Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /), 
    то выведите результат применения этой операции к введённым ранее числам, в противном случае 
    выведите «Неверная операция» (без кавычек). Если пользователь захочет поделить на ноль, выведите 
    текст «На ноль делить нельзя!» (без кавычек).

    Формат входных данных
    На вход программе подаются два целых числа и строка, всё на отдельной строке.

    Формат выходных данных
    Программа должна вывести результат применения операции к введенным числам или соответствующий текст, 
    если операция неверная либо если происходит деление на ноль.

    Sample Input 1:
    6104
    0
    /
    Sample Output 1:
    На ноль делить нельзя!
"""
a1, b1, c1 = int(input()), int(input()), input(),

if c1=="+":
    a1+=b1 
    print(a1)
elif c1=="-":
    a1-=b1 
    print(a1)
elif c1=="*":
    a1*=b1 
    print(a1)
elif c1=="/"and b1!=0:
    a1/=b1 
    print(a1)
elif c1=="/"and b1==0:
    print("На ноль делить нельзя!")
else : 
    print("Неверная операция")