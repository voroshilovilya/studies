"""
    В операционной системе Windows полное имя файла состоит из буквы диска, после которого 
    ставится двоеточие и символ  "\",  затем через такой же символ перечисляются подкаталоги 
    (папки), в которых находится файл, в конце пишется имя файла (C:\Windows\System32\calc.exe).

    На вход программе подается одна строка с корректным именем файла в операционной системе Windows. 
    Напишите программу, которая разбирает строку на части, разделенные символом "\". 
    Каждую часть вывести в отдельной строке.

    Формат входных данных
    На вход программе подается одна строка.

    Формат выходных данных
    Программа должна вывести текст в соответствии с условием задачи.

    Примечание. В Python символ \ обычно используется для создания специальных символьных 
    последовательностей, которые представляют собой управляющие символы или экранированные 
    последовательности. Например, \n представляет символ новой строки, \t представляет 
    символ табуляции и т.д. Однако если символ \ используется как часть строки, его следует 
    экранировать, т.е. использовать два обратных слэша \\.

    Sample Input:
    C:\Windows\System32\calc.exe
    Sample Output:
    C:
    Windows
    System32
    calc.exe
"""
n = input().split("\\")
print(*n, sep = "\n")