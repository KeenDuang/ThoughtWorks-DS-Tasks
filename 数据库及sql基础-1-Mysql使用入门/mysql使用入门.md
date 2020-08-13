- 数据库创建

 `CREATE DATABASE student_examination_sys;`

- 数据表创建

```
---选择数据库
use student_examination_sys;
---学生表
CREATE TABLE IF NOT EXISTS student(
     id   VARCHAR(40),
     name VARCHAR(40),
     age  INT,
     sex  VARCHAR(10),
     PRIMARY KEY (id)
  );
---考试科目表
CREATE TABLE IF NOT EXISTS subject(
     id       VARCHAR(40),
     subject  VARCHAR(40),
     teacher  VARCHAR(40),
     description  VARCHAR(100),
     PRIMARY KEY (ID)
  );
---成绩表
CREATE TABLE IF NOT EXISTS score(
     id       VARCHAR(40),
     student_id  VARCHAR(40),
     subject_id  VARCHAR(40),
     score  DECIMAL(4,1),
     PRIMARY KEY (ID)
  );
```

- 插入数据

```
---学生表
INSERT INTO student
       (id, name, age, sex)
VALUES
       ('001', '张三', 18, '男'),
       ('002', '李四', 20, '女');
---考试科目表
INSERT INTO subject
       (id, subject, teacher, description)
VALUES
       ('1001', '语文', '王老师', '本次考试比较简单'),
       ('1002',	'数学', '刘老师', '本次考试比较难');
---成绩表
INSERT INTO score
       (id, student_id, subject_id, score)
VALUES
       ('1', '001', '1001', 80),
       ('2', '002',	'1002',	60),
       ('3', '001',	'1001',	70),
       ('4', '002',	'1002',	60.5);
```

