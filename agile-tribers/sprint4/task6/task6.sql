use task3;
CREATE TABLE Library (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    genre VARCHAR(50),
    price INT,
    publish_year INT,
    copies INT
);

INSERT INTO Library (book_id, title, author, genre, price, publish_year, copies) VALUES
(1, 'The Silent Patient', 'Alex Michaelides', 'Thriller', 350, 2019, 5),
(2, 'Becoming', 'Michelle Obama', 'Biography', 500, 2018, 2),
(3, 'Atomic Habits', 'James Clear', 'Self-help', 400, 2018, 4),
(4, 'The Alchemist', 'Paulo Coelho', 'Fiction', 300, 1988, 6),
(5, 'It Ends With Us', 'Colleen Hoover', 'Romance', 275, 2016, 3),
(6, 'Rich Dad Poor Dad', 'Robert Kiyosaki', 'Finance', 450, 2000, 1),
(7, 'The Power of Habit', 'Charles Duhigg', 'Self-help', 380, 2012, 5),
(8, 'The Psychology of Money', 'Morgan Housel', 'Finance', 450, 2020, 4),
(9, 'Verity', 'Colleen Hoover', 'Thriller', 350, 2018, 2),
(10, 'Outliers', 'Malcolm Gladwell', 'Self-help', 360, 2008, 3);
#1
select * from Library where price= (select max(price) from Library );
#2
select * from Library where publish_year<(select avg(publish_year) from Library);
#3
select * from Library where copies>(select copies from Library where title='Becoming'  );
#4
select * from library where genre=(select genre from library where title='Atomic Habits' );
#5
select* from Library where copies<all(select copies from Library where genre='Self-help' );
#6
select* from library where price in (select price from Library group by price having count(price)>1 );
#7
select* from Library where publish_year =(select min(publish_year) from library);
#8
select * from library where author in (select author from library group by author having count(author)>1);
#9
select * from library where price>(select avg(price)from library);
#10
select * from library where publish_year=(select publish_year from library where title='The Power of Habit');