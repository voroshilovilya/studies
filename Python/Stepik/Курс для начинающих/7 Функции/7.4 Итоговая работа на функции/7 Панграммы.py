"""
    Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы используют 
    для презентации шрифтов, чтобы можно было в одной фразе рассмотреть все глифы.

    Напишите функцию, is_pangram(text) которая принимает в качестве аргумента строку текста 
    на английском языке и возвращает значение True если текст является панграммой и False в противном случае.

    Примечание 1. Гарантируется, что введенная строка содержит только буквы английского алфавита и пробелы.

    Примечание 2. Следующий программный код:
    print(is_pangram('Jackdaws love my big sphinx of quartz'))
    print(is_pangram('The jay pig fox zebra and my wolves quack'))
    print(is_pangram('Hello world'))

    должен выводить:
    True
    True
    False
"""
def is_pangram(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    t = text.lower()
    if len(t) <26: return False
    else :
        for i in range(26):
            if abc[i] in t: continue
            else: return False
        return True
         
# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))