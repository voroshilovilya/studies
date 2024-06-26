/*
Придумайте один или несколько запросов к нашей таблице book, используя групповые функции. 
Проверьте, правильно ли они работают.

Структура и наполнение таблицы book:

book_id	title	author	price	amount
INT PRIMARY KEY AUTO_INCREMENT	VARCHAR(50)	VARCHAR(30)	DECIMAL(8,2)	INT
1	Мастер и Маргарита	Булгаков М.А.	670.99	3
2	Белая гвардия	Булгаков М.А.	540.50	5
3	Идиот	Достоевский Ф.М.	460.00	10
4	Братья Карамазовы	Достоевский Ф.М.	799.01	3
5	Игрок	Достоевский Ф.М.	480.50	10
6	Стихотворения и поэмы	Есенин С.А.	650.00	15
*/
SELECT author,
       COUNT(title) AS количество_произведений,
       MIN(price) AS минимальная_цена,
       SUM(amount) AS количество_книг
  FROM book
  
 GROUP BY author
HAVING COUNT(title) > 1
   AND SUM(amount) > 1
   AND MIN(price) > 500
/* 
Узнать сколько авторов, у которых есть книги со стоимостью более 500 и количеством более 1 шт на складе, 
при количестве различных названий произведений не менее 2-х. Вывести автора, количество различных 
произведений автора, минимальную цену и количество книг на складе.
*/