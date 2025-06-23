create database task3;
show databases;
use task3;
 create table employee(
 employeeid int,
 firstname varchar(50),
 lastname varchar(50),
 department varchar(50),
 salary decimal(10,2),
 hire_date date);
insert into employee(employeeid,firstname,lastname,department,salary,hire_date)values
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

select department,avg(salary) as average_salary from employee group by department having avg(salary)>60000;
use task3;
select department from employee group by department having avg(salary)>55000 and count(employeeid)>2;
select department from employee group by department having sum(salary)>50000;
select*from employee where department in(select department from employee group by department having min(salary)>45000);
select*from employee order by firstname asc;
select*from employee order by hire_date desc;
select employeeid,firstname,lastname,salary from employee order by salary asc;
select department,sum(salary) as total_salary from employee group by department;
select department,avg(salary) as avg_salary from employee group by department;
select department,count(employeeid) as employee_count from employee group by department;
select department,max(salary) as highest_salary from employee group by department;
select year(hire_date),sum(salary) as total_salary from employee group by year(hire_date);
select*from employee;
