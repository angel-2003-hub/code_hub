create database StudentDetails;
show databases;
/**/
#to create the table
create table students(StudentId int primary key,
Name varchar(20) not null,
Grade varchar(10) ,
Age int not null);
select * from students;

#to add column in the table
alter table students add Grade varchar(50) not null;

alter table students add Email varchar(50) not null;
#To delete column
alter table students drop column Grade;
#to change column datatype
alter table students modify column Age varchar(3);

#to rename the table


alter table students rename to StudentDetails;

truncate table StudentDetails;
USE StudentDetails;
create table Employees(EmpID int primary key,
EmpName varchar(20),
EmpSalary varchar(100));

alter table Employees add Department varchar(50);
drop table Employees;

create table Products(ProductID int primary key,ProductName varchar(50),price varchar(50));
select*from Products;
create table Books(BookID int,
Title varchar(50),
Author varchar(50),
PublishedYear varchar(20));

insert into Books(BookID,Title,Author,PublishedYear) values(1,'The Great Gatesby','f.scott fitzgerald',1925),
(2,'Moby-Dick','Herman Melville',1851),(3,'Learning SQL','Alan BeaulieuO',2020),
(4,"SQL For Dummies",'Allen G. Taylor',2022),(5,'Head First SQL','Lynn Beighley',2007),
(6,'SQL Cookbook','Anthony Molinaro',2020),(7,"Practical SQL",'Anthony DeBarros',2022),
(8,'The Art of SQL','Stéphane Faroult, Peter Robson',2006),
(9,'SQL Antipatterns','Bill Karwin',2010),
(10,"T-SQL Fundamentals","Itzik Ben-Gan",2016);

select Title,Author from Books;

UPDATE Books SET Author='F.S.Fitzgerald' WHERE BookID = 1 LIMIT 1;

#To delete a specific row
delete from Books where BookID=2 limit 1;

create table employees(employee_id integer primary key,
first_name varchar(50),
last_name varchar(50),
age integer,
department varchar(50),
salary decimal(10,2) );
insert into employees(employee_id,first_name,last_name,age,department,salary)values
(1,'John','Doe',30,'HR',50000),
(2,'Jane','Smith',25,'Finance',60000),
(3,'Alice','Johnson',28,'IT',70000);
update employees set salary=50000 where employee_id=2 limit 1;

delete from employees where employee_id=3 limit 1;

insert into employees(employee_id,first_name,last_name,age,department,salary)values(4,'Michael','Taylor',35,'Sales',75000.00),
(5,'Emily','Davis',40,'Marketing',80000.00);
use StudentDetails;
insert into employees(employee_id,first_name,last_name,age,department,salary)values
(6,'David','Wilson',32,'IT',72000),(7,'Laura','Brown',29,'HR',51000),
(8,'Chris','Andrson',27,'Finance',59000),(9,'Emma','Thomas',38,'Sales',78000),
(10,'Daniel','Clerk',33,'Marketing',81000);

select*from employees; 


