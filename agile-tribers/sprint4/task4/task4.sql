use task3;
#1
create table mark(markid int,
studentid int,
subject varchar(50),
marks int
);
insert into mark(markid,studentid,subject,marks)values(1,1,'Math',85),
(2,2,'Science',78),
(3,3,'English',90),
(4,4,'History',88),
(5,5,'geography',92);
select*from mark;
create table student(
studentid int,
name varchar(50),
age int,
class varchar(50)
);
insert into student(studentid,name,age,class)values
(1,'Alice',14,'8A'),
(2,'Bob',15,'9B'),
(3,'Charlie',13,'7A'),
(4,'David',14,'8B'),
(5,'Eva',15,'9A');

select*from student;

select student.name from mark inner join student on student.studentid=mark.studentid;
SELECT DISTINCT s.name
FROM student s
INNER JOIN mark m ON s.studentid = m.studentid
WHERE m.marks IS NOT NULL;
use task3;
select s.name,m.subject,m.marks from student as s  inner join mark as m on s.studentid=m.studentid where m.marks>85 limit 5 ;
select s.name,m.subject from student as s inner join mark as m on  s.studentid=m.studentid order by s.name asc;
#2
select s.name,m.subject,m.marks from student as s inner join mark as m on  s.studentid=m.studentid;
select s.name,m.marks from student as s inner join mark as m on  s.studentid=m.studentid;
select s.name,m.subject,m.marks ,case when m.marks is null then'Not Avaliable' end  from student as s left join mark as m on s.studentid=m.studentid  ;
select s.name,m.subject,m.marks from student as s left join mark as m on s.studentid=m.studentid where s.age>14 ;
#3
select s.name,m.marks from student as s right join mark as m on s.studentid=m.studentid ;   #11
select m.subject,s.name from student as s right join mark as m on s.studentid=m.studentid ;  #12
select m.subject,s.name from student as s right join mark as m on s.studentid=m.studentid ;  #13
select s.name,m.marks,m.subject from student as s right join mark as m on s.studentid=m.studentid where m.subject='English';
select m.markid,m.subject,m.marks,s.name from student as s right join mark as m on s.studentid=m.studentid;
#4
select s.name,m.subject,m.marks from student as s left join mark as m on s.studentid=m.studentid
union 
select s.name,m.subject,m.marks from student as s right join mark as m on s.studentid=m.studentid;

select s.name,m.marks from student as s left join mark as m on s.studentid=m.studentid
union 
select s.name,m.marks from student as s right join mark as m on s.studentid=m.studentid;
use task3;
 
SELECT 
    COALESCE(s.name, 'No Data Available') AS student_name,
    COALESCE(CAST(m.marks AS CHAR), 'No Data Available') AS mark_data
FROM 
    student s
LEFT JOIN 
    mark m ON s.studentid = m.studentid

UNION

SELECT 
    COALESCE(s.name, 'No Data Available') AS student_name,
    COALESCE(CAST(m.marks AS CHAR), 'No Data Available') AS mark_data
FROM 
    student s
RIGHT JOIN 
    mark m ON s.studentid = m.studentid;
    
    
    
SELECT 
    s.name AS student_name,
    'No Mark Found' AS info
FROM 
    student s
LEFT JOIN 
    mark m ON s.studentid = m.studentid
WHERE 
    m.studentid IS NULL

UNION

-- Marks without students
SELECT 
    'No Student Found' AS student_name,
    CONCAT('Mark: ', m.marks) AS info
FROM 
    student s
RIGHT JOIN 
    mark m ON s.studentid = m.studentid
WHERE 
    s.studentid IS NULL;
