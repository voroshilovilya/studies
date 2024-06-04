"""
    Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента 
    непустую строку text, состоящую из символов ( и ) и возвращает значение True если 
    поступившая на вход строка является правильной скобочной последовательностью 
    и False в противном случае.

    Примечание 1. Правильной скобочной последовательностью называется строка, состоящая 
    только из символов ( и ), где каждой открывающей скобке найдется парная закрывающая 
    скобка (при этом каждая открывающая скобка должна быть левее соответствующей ей 
    закрывающей скобки).

    Примечание 2. Следующий программный код:
    print(is_correct_bracket('()(()())'))
    print(is_correct_bracket(')(())('))

    должен выводить:
    True
    False

    Sample Input:
    ((()))
    Sample Output:
    True
"""
def is_correct_bracket(text):
    count = 0
    for i in range(len(text)):
        if text[i] == "(" : count+=1
        elif text[i] == ")" : 
            count-=1
            if count < 0:
                return False       
    if count == 0:return True
    else: return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))