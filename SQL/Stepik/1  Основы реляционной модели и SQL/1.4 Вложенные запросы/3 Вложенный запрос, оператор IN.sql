/*
Вывести информацию (автора, книгу и количество) о тех книгах, количество экземпляров которых в таблице book не дублируется.

Результат
+---------------+-----------------------+--------+
| author        | title                 | amount |
+---------------+-----------------------+--------+
| Булгаков М.А. | Белая гвардия         | 5      |
| Есенин С.А.   | Стихотворения и поэмы | 15     |
+---------------+-----------------------+--------+
Пояснение к решению
Во вложенном запросе отберите те значения столбца amount, количество которых, вычисленное с помощью функции count(), равно 1. 

Структура и наполнение таблицы book
+---------+-----------------------+------------------+--------+--------+
| book_id | title                 | author           | price  | amount |
+---------+-----------------------+------------------+--------+--------+
| 1       | Мастер и Маргарита    | Булгаков М.А.    | 670.99 | 3      |
| 2       | Белая гвардия         | Булгаков М.А.    | 540.50 | 5      |
| 3       | Идиот                 | Достоевский Ф.М. | 460.00 | 10     |
| 4       | Братья Карамазовы     | Достоевский Ф.М. | 799.01 | 3      |
| 5       | Игрок                 | Достоевский Ф.М. | 480.50 | 10     |
| 6       | Стихотворения и поэмы | Есенин С.А.      | 650.00 | 15     |
+---------+-----------------------+------------------+--------+--------+
*/
SELECT author, title, amount 
  FROM book
 WHERE amount IN ( 
                   SELECT amount 
                     FROM book
                    GROUP BY amount
                   HAVING COUNT(amount) = 1 
                 )