/*
Придумайте один или несколько запросов корректировки данных к  таблицамbook и  supply . Проверьте, правильно ли они работают.

Структура и наполнение таблиц:

Таблица book

book_id	title	author	price	amount
1	Мастер и Маргарита	Булгаков М.А.	670.99	3
2	Белая гвардия	Булгаков М.А.	540.50	5
3	Идиот	Достоевский Ф.М.	460.00	10
4	Братья Карамазовы	Достоевский Ф.М.	799.01	2
5	Стихотворения и поэмы	Есенин С.А.	650.00	15
Таблица supply :

supply_id	title	author	price	amount
1	Лирика	Пастернак Б.Л.	518.99	2
2	Черный человек 	Есенин С.А.	570.20	6
3	Белая гвардия	Булгаков М.А.	540.50	7
4	Идиот	Достоевский Ф.М.	360.80	3
*/
UPDATE book AS b1
   SET b1.price = b1.price * 0.95
 WHERE b1.amount = (SELECT MAX(b2.amount) from (select * from book) as b2);

SELECT *
  FROM book

--Делаем скидку 5% на самое большое количество экземпляров книг (Стихи Есенина), чтобы поскорее расходились.