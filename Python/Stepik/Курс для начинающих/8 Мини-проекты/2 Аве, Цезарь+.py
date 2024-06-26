"""
    На вход программе подается строка текста на английском языке, в которой нужно 
    зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра 
    Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются 
    строчными, а прописные – прописными. Гарантируется, что между различными словами 
    присутствует один пробел.

    Формат входных данных 
    На вход программе подается строка текста на английском языке.

    Формат выходных данных
    Программа должна вывести зашифрованный текст в соответствии с условием задачи.

    Примечание. Символы, не являющиеся английскими буквами, не изменяются.

    Sample Input 1:
    Day, mice. "Year" is a mistake!
    Sample Output 1:
    Gdb, qmgi. "Ciev" ku b tpzahrl!
"""
import string

# Очищаем слово от символов
def removed_chars(s):
    del_chars = ',.!#$:()"~@%;?'
    return s.translate(str.maketrans('', '', del_chars))

def encrypt_word(word):
    """
    Функция шифрует слово с помощью шифра Цезаря с циклическим сдвигом на длину слова.
    """
    word_clear = removed_chars(word) # Очищаем слово от символов
    shift = len(word_clear) # Длина слова без символов
    lower_alphabet = string.ascii_lowercase # Получаем алфавит в нижнем регистре
    upper_alphabet = string.ascii_uppercase # Получаем алавит в верхнем регистре
    encrypted = "" # Создаем пустой список в который будем добавлять шифрованные буквы
    for char in word:
        if char in lower_alphabet:
            # Шифруем строчные буквы
            encrypted += lower_alphabet[(lower_alphabet.index(char) + shift) % 26]
        elif char in upper_alphabet:
            # Шифруем прописные буквы
            encrypted += upper_alphabet[(upper_alphabet.index(char) + shift) % 26]
        else:
            # Оставляем не буквенные символы как есть
            encrypted += char
    return encrypted

def encrypt_sentence(sentence):
    """
    Функция шифрует все слова в предложении с помощью шифра Цезаря.
    """
    words = sentence.split()
    encrypted_words = []
    for word in words:
        encrypted_word = encrypt_word(word)
        encrypted_words.append(encrypted_word)
    return " ".join(encrypted_words)


# Ввод фразы и вывод шифрованой
sentence = input().strip()
print(encrypt_sentence(sentence))