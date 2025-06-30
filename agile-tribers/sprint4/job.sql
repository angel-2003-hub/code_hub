SELECT * FROM education.`employee info`;
alter table `employee info` rename to employee_info;
use education;
select * from employee_info;
#1
select * from employee_info where Gender='Male' and  Age<30 and EverBenched='No';
#2
select avg(Age) from employee_info where LeaveOrNot=1; 
#3
select Education,count(Education) from  employee_info where ExperienceInCurrentDomain>1 group by Education ;
#4
use education;
select city,count(*) as employee_count ,rank() over (order by  count(*) desc) AS city_rank from employee_info group by City ;
#5
select city ,Gender, count(*)from employee_info as gender_count group by City,Gender order by City;
#6
select JoiningYear,count(*) as total_emp,avg(ExperienceInCurrentDomain) average_experience from employee_info group by JoiningYear;
#7
select * from employee_info where City='Bangalore' and EverBenched ='No' and PaymentTier=(select max(PaymentTier) from employee_info);
#8
use education;
SELECT ROUND(COUNT(CASE WHEN LeaveOrNot = 1 THEN 1 END) / COUNT(*) * 100, 2) AS benched_percent
FROM 
    employee_info
WHERE 
    EverBenched = 'Yes';
#9
select * ,
	case 
		when classification=1 then 'senior'
		when classification=2 then 'Mid'
		when classification=3 then 'Junior'
	end as class 
from(
select *,
	ntile(3) over(order by ExperienceInCurrentDomain desc) as classification 
from employee_info) as ranked;
#10
select EverBenched,LeaveOrNot,count(*) as employees from employee_info group by EverBenched,LeaveOrNot;
#11
with min_age as(select * ,row_number() over(partition by City order by Age asc) as row_coln 
from employee_info)select City,Age from min_age where row_coln=1;
#12
select City ,avg(Age) as avg_age from employee_info  group by City having avg(age)>30; ##
#13
select Age,city,avg(city) over(partition by City) as avg_age from employee_info ;##
#14

select City,Age ,case when Age<25 then 'Young' when Age between 25 and 35 then 'Adult' when Age>35 then 'Senior' end as AgeGroup from employee_info;
#15
use education;
select ExperienceInCurrentDomain,PaymentTier,Age,City from employee_info 
where (ExperienceInCurrentDomain<2 and PaymentTier=3) or (Age>30 and City='Pune');  
#16
CREATE TABLE CitySalaryAvg (
    City VARCHAR(100),
    AvgSalary DECIMAL(10, 2)
);
INSERT INTO CitySalaryAvg (City, AvgSalary) VALUES
('Pune', 60000.00),
('Bangalore', 55000.00),
('New Delhi', 50000.00),
('Bihar', 65000.00),
('Chennai', 48000.00);
SELECT 
    e.City,
    e.PaymentTier,
    c.AvgSalary
FROM 
    employee_info e
JOIN 
    CitySalaryAvg c ON e.City = c.City
WHERE 
    e.PaymentTier > c.AvgSalary;


select * from CitySalaryAvg;
#17
SELECT ExperienceInCurrentDomain, Education 
FROM employee_info 
WHERE 
    ExperienceInCurrentDomain IS NULL OR ExperienceInCurrentDomain = '' OR ExperienceInCurrentDomain = 'N/A' OR ExperienceInCurrentDomain = 'None'
    OR
    Education IS NULL OR Education = '' OR Education = 'N/A' OR Education = 'None';
#18
select Age,City from(select Age,City, ntile(5) over(order by Age desc) as top_percent from  employee_info ) as per_per where top_percent = 1;
#19
select EverBenched,LeaveOrNot ,count(*) from employee_info group by EverBenched , LeaveOrNot ;
#20
SELECT COUNT(*) AS unique_combinations
FROM (
    SELECT DISTINCT City, PaymentTier
    FROM employee_info
) AS distinct_combinations;
#21
select Gender,count(Gender) as total from employee_info where LeaveOrNot=1 group by Gender ;
#22
select Age,ExperienceInCurrentDomain ,(Age-ExperienceInCurrentDomain) as difference  from employee_info where (Age-ExperienceInCurrentDomain)>30 ;
#23
select JoiningYear ,round(sum(LeaveOrNot=0)/count(LeaveOrNot)*100) as employee_stayed from employee_info group by JoiningYear ;
#24
use education;
select City,avg(ExperienceInCurrentDomain) as highest_average from employee_info where EverBenched='No' group by City order by avg(ExperienceInCurrentDomain) desc limit 1 ;
#25
select EverBenched,ExperienceInCurrentDomain,case when EverBenched='Yes' and  ExperienceInCurrentDomain<3 then 'Yes'
else 'No' end as LikelyToLeave from employee_info;
