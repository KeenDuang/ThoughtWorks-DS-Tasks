create table student(id int(10),name varchar(10),age datetime,sex varchar(10));

insert into student values(1 , '赵雷' , '1990-01-01' , '男');
insert into student values(2 , '钱电' , '1990-12-21' , '男');
insert into student values(3 , '孙风' , '1990-05-20' , '男');
insert into student values(4 , '李云' , '1990-08-06' , '男');
insert into student values(5 , '周梅' , '1991-12-01' , '女');
insert into student values(6 , '吴兰' , '1992-03-01' , '女');
insert into student values(7 , '郑竹' , '1989-07-01' , '女');
insert into student values(8 , '王菊' , '1990-01-20' , '女');

create table course(id int(10),name varchar(10),teacherId int(10));
insert into course values(1 , '语文' , 2);
insert into course values(2 , '数学' , 1);
insert into course values(3 , '英语' , 3);

create table teacher(id int(10),name varchar(10));
insert into teacher values(1 , '张三');
insert into teacher values(2 , '李四');
insert into teacher values(3 , '王五');

create table student_course(studentId int(10),courseId varchar(10),score decimal(18,1));
insert into student_course values(1 , 1 , 80);
insert into student_course values(1 , 2 , 90);
insert into student_course values(1 , 3 , 99);
insert into student_course values(2 , 1 , 70);
insert into student_course values(2 , 2 , 60);
insert into student_course values(2 , 3 , 80);
insert into student_course values(3 , 1 , 80);
insert into student_course values(3 , 2 , 80);
insert into student_course values(3 , 3 , 80);
insert into student_course values(4 , 1 , 50);
insert into student_course values(4 , 2 , 30);
insert into student_course values(4 , 3 , 20);
insert into student_course values(5 , 1 , 76);
insert into student_course values(5 , 2 , 87);
insert into student_course values(6 , 1 , 31);
insert into student_course values(6 , 3 , 34);
insert into student_course values(7 , 2 , 89);
insert into student_course values(7 , 3 , 98);
