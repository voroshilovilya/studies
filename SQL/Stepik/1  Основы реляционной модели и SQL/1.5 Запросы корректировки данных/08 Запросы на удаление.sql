/*
Удалить из таблицы supply книги тех авторов, общее количество экземпляров книг которых в таблице book превышает 10.

Результат
Affected rows: 2

Query result:
+-----------+---------------+----------------+--------+--------+
| supply_id | title         | author         | price  | amount |
+-----------+---------------+----------------+--------+--------+
| 1         | Лирика        | Пастернак Б.Л. | 518.99 | 2      |
| 3         | Белая гвардия | Булгаков М.А.  | 540.50 | 7      |
+-----------+---------------+----------------+--------+--------+
Структура и наполнение таблиц book и supply
+---------+-----------------------+------------------+--------+--------+
| book_id | title                 | author           | price  | amount |
+---------+-----------------------+------------------+--------+--------+
| 1       | Мастер и Маргарита    | Булгаков М.А.    | 670.99 | 3      |
| 2       | Белая гвардия         | Булгаков М.А.    | 540.50 | 5      |
| 3       | Идиот                 | Достоевский Ф.М. | 460.00 | 10     |
| 4       | Братья Карамазовы     | Достоевский Ф.М. | 799.01 | 2      |
| 5       | Стихотворения и поэмы | Есенин С.А.      | 650.00 | 15     |
+---------+-----------------------+------------------+--------+--------+
+-----------+----------------+------------------+--------+--------+
| supply_id | title          | author           | price  | amount |
+-----------+----------------+------------------+--------+--------+
| 1         | Лирика         | Пастернак Б.Л.   | 518.99 | 2      |
| 2         | Черный человек | Есенин С.А.      | 570.20 | 6      |
| 3         | Белая гвардия  | Булгаков М.А.    | 540.50 | 7      |
| 4         | Идиот          | Достоевский Ф.М. | 360.80 | 3      |
+-----------+----------------+------------------+--------+--------+
*/
DELETE FROM supply
 WHERE author IN (
                  SELECT author
                    FROM book
                   GROUP BY author
                  HAVING SUM(amount) > 10
                 ); 
SELECT *
  FROM supply