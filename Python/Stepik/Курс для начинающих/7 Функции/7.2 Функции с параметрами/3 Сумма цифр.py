"""
    Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
    
    Sample Input 1:
    12345
    Sample Output 1:
    15
"""
def print_digit_sum(num):
    n = [int(i)  for  i  in  str(num)]
    print(sum(n))
    pass

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)