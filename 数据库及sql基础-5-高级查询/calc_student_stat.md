#### 数据库创建

```drop database if exists student_examination_sys_new;
create database student_examination_sys_new;
use student_examination_sys_new;
```

#### 数据表创建

```drop table if exists student;
--student表
create table  student  
(id     varchar(5)  not null,
 name   varchar(10),
 age    int,
 sex    varchar(1)
);

--subject表
create table  subject  
(id           int  not null,
 subject      varchar(10),
 teacher      varchar(10),
 description  varchar(20)
);

--score表
create table  score  
(id           int  not null,
 student_id   varchar(5),
 subject_id   int,
 score        float
);

insert into student(id,name,age,sex)
values( '001','张三',18,'男'),('002','李四',20,'女');
```

#### 数据插入

```
--student表
insert into student(id,name,age,sex)
values( '001','张三',18,'男'),('002','李四',20,'女');

--subject表
insert into subject(id,subject,teacher,description)
values( 1001,'语文','王老师','本次考试比较简单'),(1002,'数学','刘老师','本次考试比较难');

--score表
insert into score(id,student_id,subject_id,score)
values( 1,'001',1001,80),(2,'002',1001,75),(3,'001',1002,70),(4,'002',1002,60.5);
```

#### 数据查询

请编写一个MySQL存储过程`calc_student_stat`计算统计数据并输出到一个新表`student_stat`中。其中需要统计的数据有：

- avg_score: 该科目平均分

- score: 学生在该科目下的得分

- total_score: 学生总分

- score_rate: 该科目得分占总分的比例

除了上述统计字段，`student_stat`表还包含字段：`name` `teacher` `subject`.  

```drop procedure if exists calc_student_stat;
delimiter $$
create procedure calc_student_stat()
BEGIN
  drop temporary table if exists student_stat_temp;
  create temporary table student_stat_temp as
  select 
    t1.student_id, t1.subject_id,t1.score, t2.total_score,t3.avg_score,t1.score/t2.total_score as score_rate 
  from score t1
  left join
   (select student_id,sum(score) as total_score 
    from score 
    group by student_id) t2 
  on t1.student_id = t2.student_id
  left join 
   (select subject_id,avg(score) as avg_score
    from score 
    group by subject_id) t3
  on t1.subject_id = t3.subject_id;

  drop table if exists student_stat;
  create table student_stat as
  select 
    b.name,c.subject,c.teacher,a.score, a.total_score,a.avg_score,a.score_rate
  from student_stat_temp a
  left join student b
  on a.student_id = b.id
  left join subject c
  on a.subject_id = c.id;
END $$

delimiter ;
call calc_student_stat();
```