# 1.查询同时存在1课程和2课程的情况
select 
      t1.studentId as StudentId
      ,t3.name as name
      ,t3.age as age
      ,t3.sex as sex
      ,t1.score as score_course1
      ,t2.score as score_course2
from
(select * from student_course where courseId=1) t1
inner join
(select * from student_course where courseId=2) t2
on t1.studentId=t2.studentId
left join student t3
on t1.studentId=t3.id;

# 2.查询同时存在1课程和2课程的情况
同上

# 3.查询平均成绩大于等于60分的同学的学生编号和学生姓名和平均成绩
select
      t1.studentId, t2.name, t1.score_avg
from
(select studentId, avg(score) as score_avg  from student_course group by studentId) t1
left join student t2
on t1.studentId=t2.id
where t1.score_avg>=60
order by t1.score_avg desc;

# 4.查询在student_course表中不存在成绩的学生信息的SQL语句
select t1.studentId  
from student_course t1
left join
student t2
on t1.studentId=t2.id
where t2.id is null;

# 5.查询所有有成绩的SQL
select * from student_course;

# 6.查询学过编号为1并且也学过编号为2的课程的同学的信息
select 
      t1.studentId as StudentId
      ,t3.name as name
      ,t3.age as age
      ,t3.sex as sex
      ,t1.score as score_course1
      ,t2.score as score_course2
from
(select * from student_course where courseId=1) t1
inner join
(select * from student_course where courseId=2) t2
on t1.studentId=t2.studentId
left join student t3
on t1.studentId=t3.id;

# 7.检索1课程分数小于60，按分数降序排列的学生信息
select 
     t1.studentId, t2.name, t2.sex, t2.age, t1.score
from student_course  t1
left join student t2
on t1.studentId=t2.id
where t1.courseId=1 and t1.score<60
order by t1.score desc;

# 8.查询每门课程的平均成绩，结果按平均成绩降序排列，平均成绩相同时，按课程编号升序排列
select 
	courseId, avg(score) as score_avg  
from student_course  
group by courseId 
order by score_avg desc, courseId asc;

# 9.查询课程名称为"数学"，且分数低于60的学生姓名和分数
elect t3.name, t1.score
from student_course t1
inner join course t2
on t1.courseId=t2.id and t2.name='数学'
left join student t3
on t1.studentId=t3.id
where t1.score<60
order by t1.score desc;
