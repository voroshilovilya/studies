"""
    Напишите функцию is_password_good(password), которая принимает в качестве аргумента 
    строковое значение пароля password и возвращает значение True, если пароль является 
    надежным и False - в противном случае.

    Пароль является надежным если:
    его длина не менее 8 символов; 
    он содержит как минимум одну заглавную букву (верхний регистр); 
    он содержит как минимум одну строчную букву (нижний регистр);
    он содержит хотя бы одну цифру.

    Примечание. Следующий программный код:
    print(is_password_good('aabbCC11OP'))
    print(is_password_good('abC1pu'))

    должен выводить:
    True
    False
"""
def is_password_good(pw):
    if len(pw) >= 8 and pw != pw.upper() and pw != pw.lower() :
        for i in range(len(pw)):
            if pw[i] in "0123456789" : return True
        return False
    else : return False
    
# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))