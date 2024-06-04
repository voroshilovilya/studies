"""
    BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.

    Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. 
    Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
    число a – должно быть палиндромом;
    число b – должно быть простым;
    число c – должно быть четным.

    Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое 
    значение пароля password и возвращает значение True, если пароль является действительным паролем 
    BEEGEEK банка и False - в противном случае.

    Примечание. Следующий программный код:
    print(is_valid_password('1221:101:22'))
    print(is_valid_password('565:30:50'))
    print(is_valid_password('112:7:9'))
    print(is_valid_password('1221:101:22:22'))

    должен выводить:
    True
    False
    False
    False

    Sample Input:
    15551:7:290
    Sample Output:
    True
"""
def is_valid_password(pw):
    if pw.count(":") != 2: return False
    else :
        n = pw.split(":")
        a, b, c = n[0], n[1], n[2]
        b = int(b)
        for i in range (2, b):
            if b%i == 0: return False
        if int(c)%2 !=0 : return False
        elif a != a [::-1]: return False
        else : return True

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))