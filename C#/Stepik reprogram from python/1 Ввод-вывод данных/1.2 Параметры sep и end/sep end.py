# Напишите программу, которая выводит на экран следующий текст: I***like***Python 
print("I", "like", "Python", sep="***")

# Напишите программу, которая приветствует пользователя в следующем формате: Привет, <имя пользователя>!
a = input()
print("Привет, ", a, sep="", end="!")

"""
    Напишите программу, которая считывает строку-разделитель и три строки, а затем выводит указанные 
    строки через разделитель в следующем формате:

    <вторая строка><строка-разделитель><третья строка><строка-разделитель><четвертая строка>
"""
f = input()
a = input()
s = input()
d = input()
print(a, s, d, sep=f)
