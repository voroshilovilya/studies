/*
Придумайте один или несколько запросов к нашей таблице book. Проверьте, правильно ли они работают.

Структура и наполнение таблицы book:

book_id	title	author	price	amount
INT PRIMARY KEY AUTO_INCREMENT	VARCHAR(50)	VARCHAR(30)	DECIMAL(8,2)	INT
1	Мастер и Маргарита	Булгаков М.А.	670.99	3
2	Белая гвардия	Булгаков М.А.	540.50	5
3	Идиот	Достоевский Ф.М.	460.00	10
4	Братья Карамазовы	Достоевский Ф.М.	799.01	2
5	Стихотворения и поэмы	Есенин С.А.	650.00	15
*/
SELECT "Донцова Дарья" as author,
        CONCAT("Евлампия Романова и ", title) AS title,
        ROUND(price * 1.42, 2) AS price        
  FROM book

ORDER BY price DESC, title DESC

/*
1. Сменить всех авторов на "Донцова Дарья".

2. К названию каждой книги в начале дописать "Евлампия Романова и ".

3. Цену поднять на 42%.

4. Отсортировать по убыванию цены и убыванию названия.
*/