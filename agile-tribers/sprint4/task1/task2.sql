create database Employees;
show databases;
use Employees;
#1
create table employees(
Employee_id int,
First_name varchar(50),
Last_name varchar(50),
Salary decimal(10,2),
Hire_Date  date);

alter table employees add Department varchar(50);
#2

insert into employees(Employee_id,First_name,Last_name,Salary,Hire_Date,Department)values
(1, 'Alice', 'Smith', 75000, '2018-03-01', 'Engineering'),
(2, 'Bob', 'Jones', 58000, '2019-07-15', 'HR'),
(3, 'Charlie', 'Brown', 62000, '2020-01-10', 'Engineering'),
(4, 'David', 'Wilson', 49000, '2017-05-21', 'Sales'),
(5, 'Eva', 'Taylor', 54000, '2021-11-30', 'HR'),
(6, 'Frank', 'Miller', 67000, '2022-02-12', 'Marketing'),
(7, 'Grace', 'Lee', 72000, '2019-09-09', 'Finance'),
(8, 'Henry', 'Clark', 69000, '2020-06-14', 'Engineering'),
(9, 'Irene', 'Adams', 56000, '2023-01-20', 'Marketing'),
(10, 'Jack', 'Harris', 51000, '2018-10-05', 'Sales'),
(11, 'Karen', 'Walker', 63000, '2017-12-25', 'HR'),
(12, 'Liam', 'Young', 77000, '2020-08-30', 'IT'),
(13, 'Mia', 'Hall', 68000, '2021-03-18', 'Engineering'),
(14, 'Noah', 'Allen', 60000, '2019-05-11', 'Finance'),
(15, 'Olivia', 'Wright', 71000, '2022-07-03', 'IT');
#3
select sum(salary) as total_salary from employees where salary>60000;
select avg(Salary) as Average_Salary from employees ;
select count(Salary) as count_salary from employees where salary<55000;
select max(Salary) as highest_salary from employees ;
select min(Salary) as lowest_salary from employees ;
select sum(Salary)as total_salary_hr from employees where Department='HR';
select avg(Salary) as avg_salary_eng from employees where department='Engineering';
select count(Salary) as count_salary_50000_to_70000 from employees where salary>50000 and salary<70000;
select sum(Salary)as sum_salary_under_60000 from employees where salary<60000;
select avg(Salary) as avg_salary_over_60000 from employees where salary>60000;
#4

create table books(employee_id int,
First_name varchar(50),
Last_name varchar(50),
department varchar(50),
salary int,
hire_data date);

insert into books(employee_id ,First_name,Last_name,department,salary,hire_data) values
(1, 'Alice', 'Smith', 'Engineering', 75000, '2018-03-01'),
(2, 'Bob', 'Jones', 'HR', 58000, '2019-07-15'),
(3, 'Charlie', 'Brown', 'Engineering', 62000, '2020-01-10'),
(4, 'David', 'Wilson', 'Sales', 49000, '2017-05-21'),
(5, 'Eva', 'Taylor', 'HR', 54000, '2021-11-30'),
(6, 'Frank', 'Anderson', 'Engineering', 88000, '2016-09-05'),
(7, 'Grace', 'Thomas', 'Marketing', 45000, '2022-02-14'),
(8, 'Hannah', 'Jackson', 'Sales', 67000, '2015-08-08'),
(9, 'Ian', 'White', 'Engineering', 59000, '2019-12-23'),
(10, 'Jane', 'Harris', 'HR', 61000, '2020-06-18'),
(11, 'Kyle', 'Martin', 'Marketing', 53000, '2018-10-09'),
(12, 'Lara', 'Thompson', 'Engineering', 72000, '2017-01-27'),
(13, 'Mike', 'Garcia', 'Sales', 48000, '2021-04-11'),
(14, 'Nina', 'Martinez', 'HR', 55000, '2022-07-06'),
(15, 'Oscar', 'Robinson', 'Marketing', 66000, '2019-02-28');

select sum(salary) as total_salary_over_60000 from books where salary>60000;
select avg(salary)as avg_salary_all from books;

select count(salary)as count_salary_under_55000 from books where salary<55000;
select max(salary)as highest_salary from books ;
select min(salary)as highest_salary from books ;
select sum(salary)as total_salary_hr from books where department='HR';
select avg(salary)as average_salary_Engineering from books where department='Engineering';
select count(salary)as count_salary_50000_to_70000 from books where salary>50000 and salary<70000;
select sum(salary) as total_salary_under_60000 from books where salary<60000;
select avg(salary) as total_salary_over_60000 from books where salary>60000;

CREATE TABLE Books_details (
    book_id INT,
    title varchar(100),
    author varchar(100),
    genre varchar(50),
    published_year int,
    available_copies int
);

insert into Books_details(book_id,title,author,genre,published_year,available_copies)values
(1, 'To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960, 4),
(2, '1984', 'George Orwell', 'Dystopian', 1949, 5),
(3, 'Pride and Prejudice', 'Jane Austen', 'Romance', 1813, 7),
(4, 'The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 1937, 6),
(5, 'The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 1925, 2),
(6, 'Moby Dick', 'Herman Melville', 'Adventure', 1851, 3),
(7, 'War and Peace', 'Leo Tolstoy', 'Historical', 1869, 1),
(8, 'The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 1951, 4),
(9, 'Brave New World', 'Aldous Huxley', 'Dystopian', 1932, 3),
(10, 'The Alchemist', 'Paulo Coelho', 'Philosophical', 1988, 5),
(11, 'The Lord of the Rings', 'J.R.R. Tolkien', 'Fantasy', 1954, 2),
(12, 'Jane Eyre', 'Charlotte Brontë', 'Romance', 1847, 6),
(13, 'The Odyssey', 'Homer', 'Epic', 1800, 2),
(14, 'Frankenstein', 'Mary Shelley', 'Horror', 1818, 4),
(15, 'The Road', 'Cormac McCarthy', 'Post-Apocalyptic', 2006, 3);
select*from Books_details where published_year between 1900 and 1950;

select*from Books_details where available_copies between 4 and 7;
select*from Books_details where published_year between 1800 and 1900;
select*from Books_details where published_year between 1800 and 1900 and available_copies>5;
use Employees;
select title from Books_details where title like 'The%';
select*from Books_details where author like '%Tolkien%';#wrong
select*from Books_details where genre='Fiction'limit 5; 
select*from Books_details where title like '%war%';
select*from Books_details where author like '%Tolstoy';
select title as book_title,available_copies as copies from Books_details; 
select*from Books_details as B where B.available_copies>5 limit 5;
select title,author,published_year as year_published from Books_details;
select title as book_title,author as book_author,available_copies as copies from Books_details; 
select title ,author ,available_copies as stock from Books_details where available_copies>4 limit 5; 
select*from Books_details  limit 5;
select*from Books_details order by published_year desc limit 3;
select*from Books_details  where available_copies>3 limit 7;
select*from Books_details order by author limit 10;
select*from Books_details where genre='Fantasy' limit 4;

select*from Books_details;