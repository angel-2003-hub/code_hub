use task3;
create table Orders(
orderid int,
customer varchar(50),
country varchar(50),
order_date date ,
amount decimal(10,2),
status varchar(50));
select * from Orders;
INSERT INTO Orders (orderId, customer, country, order_date, amount, status) VALUES
(1, 'Alice Johnson', 'USA', '2024-12-01', 250.00, 'Shipped'),
(2, 'Bob Smith', 'UK', '2024-12-03', 120.50, 'Pending'),
(3, 'Charlie Lee', 'Canada', '2024-12-04', 89.99, 'Cancelled'),
(4, 'Diana Prince', 'USA', '2024-12-05', 300.00, 'Delivered'),
(5, 'Ethan Brown', 'Australia', '2024-12-06', 45.75, 'Shipped'),
(6, 'Fiona Davis', 'India', '2024-12-07', 600.00, 'Processing'),
(7, 'George Wilson', 'Germany', '2024-12-08', 155.00, 'Delivered'),
(8, 'Hannah Moore', 'France', '2024-12-09', 78.40, 'Pending'),
(9, 'Ian Taylor', 'USA', '2024-12-10', 200.00, 'Shipped'),
(10, 'Julia Martin', 'UK', '2024-12-11', 130.25, 'Cancelled'),
(11, 'Kevin Walker', 'Canada', '2024-12-12', 499.99, 'Delivered'),
(12, 'Laura Scott', 'India', '2024-12-13', 90.00, 'Processing'),
(13, 'Michael Young', 'Australia', '2024-12-14', 105.80, 'Shipped'),
(14, 'Nancy Hall', 'Germany', '2024-12-15', 62.00, 'Delivered'),
(15, 'Oliver King', 'USA', '2024-12-16', 315.45, 'Pending');
#1
select *,
row_number() over (partition by country order by  order_date asc )as row_num
from Orders;
#2
select *,rank() over (partition by  country order by amount)as rank_coln from Orders;
#3
select *,dense_rank() over (partition by  country order by amount)as rank_coln from Orders;
#4

select*, ntile(4) over(partition by  country order by amount)as ntile_colunm from Orders;
#5
select *,lag(amount) over(partition by country order by amount)as previous_amount from Orders;
#6
select *,lead(amount) over(partition by country order by amount)as previous_amount from Orders;
#7
with order_rank as(
select country,amount ,
rank()over(partition by country order by order_date)as first_amount from Orders)
select*from order_rank where first_amount=1;
#8
use task3;
select * from Orders where year(order_date)=2023 limit 5;
#9
select distinct country,sum(amount) over(partition by country)as total_amount from orders  ;
#10
select distinct country,avg(amount) over(partition by country)as total_amount from orders  ;
#11
select distinct country,count(amount) over(partition by country)as total_order from orders  ;
#12
select*,row_number() over(partition by country order by order_date)as row_number_in_country from Orders;
#13
select*,cume_dist() over(partition by country order by amount)as cumlative_dist from Orders;
#14
select*, percent_rank() over (partition by country order by amount) as percentage_rank from Orders;
#15
select*,lag(amount) over(partition by country order by amount)as previous_amount,
amount-lag(amount) over(partition by country order by amount) as diff_with_previous from Orders;
#16
select orderid, customer, country, order_date, amount, status ,sum(amount)
 over(partition by country order by order_date)as running_total from Orders;
#17
with highest as(
select *, rank() over(partition by country order by amount desc) as mk from Orders   )
select *  from  highest where mk<=3;
#18
with highest as(
select *, rank() over(partition by country order by amount desc) as mk from Orders )
select *  from  highest where amount>100 and status='Shipped';
#19
select customer ,count(orderid) over(partition by customer order by customer) from Orders;
#20
select *, rank() over(partition by country order by amount) from Orders;
