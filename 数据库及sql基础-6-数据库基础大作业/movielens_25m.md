#### 数据库创建

 `CREATE DATABASE movielens_25m default character set utf8;`

#### 数据表创建

```
-- 选择数据库
use movielens_25m;
-- tag
DROP TABLE IF EXISTS tag;
CREATE TABLE IF NOT EXISTS tag(
     userid     VARCHAR(20),
     movieid    VARCHAR(20),
     tag        VARCHAR(400),
     timestamp  INT,
     PRIMARY KEY (userid, movieid, tag, timestamp)
  );
-- rating
DROP TABLE IF EXISTS rating;
CREATE TABLE IF NOT EXISTS rating(
     userid      VARCHAR(20),
     movieid     VARCHAR(20),
     rating      FLOAT,
     timestamp   INT,
     PRIMARY KEY (userid, movieid, timestamp)
  );
-- movie
DROP TABLE IF EXISTS movie;
CREATE TABLE IF NOT EXISTS movie(
     movieid     VARCHAR(20),
     title       VARCHAR(200),
     genres      VARCHAR(400),
     PRIMARY KEY (movieid)
  );
-- link
CREATE TABLE IF NOT EXISTS link(
     movieid     VARCHAR(20),
     imdbid      VARCHAR(20),
     tmbdid      VARCHAR(20),
     PRIMARY KEY (movieid)
  );
-- genome_scores
CREATE TABLE IF NOT EXISTS genome_scores(
     movieid     VARCHAR(20),
     tagid       VARCHAR(20),
     relevance   FLOAT,
     PRIMARY KEY (movieid, tagid)
  );
-- genome_tags
CREATE TABLE IF NOT EXISTS genome_tags(
     tagid       VARCHAR(20),
     tag         VARCHAR(200),
     PRIMARY KEY (tagid)
  );
```

#### 数据插入

```
-- tag
load data infile 'F:/Projects/ml-25m/tags.csv'
into table tag
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n'
(userid, movieid, tag, timestamp);

-- rating
load data infile 'F:/Projects/ml-25m/ratings.csv'
into table rating
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n'
ignore 1 lines
(userid, movieid, rating, timestamp);

-- movie
load data infile 'F:/Projects/ml-25m/movies.csv'
into table movie
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n'
(movieid, title, genres);
  
-- link
load data infile 'F:/Projects/ml-25m/links.csv'
into table link
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n'
(movieid, imdbid, tmbdid);
```

#### 数据查询

##### 一共有多少不同的客户
```
select t1.userid from tag t1
union
select t2.userid from rating t2
```
##### 一共有多少不同的电影

```
select count(distinct t.movieid)
from movie t
```

##### 一共有多少不同的电影种类

参考资料：

[参考资料1](https://blog.csdn.net/a5601564/article/details/70208794/)

[参考资料2](https://blog.csdn.net/zhu7478848/article/details/92794825)

```
-- 全局设置
SET GLOBAL log_bin_trust_function_creators = 1;

-- 创建临时表
DROP TABLE IF EXISTS tmp_genres; 
create temporary table tmp_genres (genre varchar(100) not null);

DELIMITER $$
-- 创建函数(统计字符串分割后单元数)
DROP FUNCTION IF EXISTS get_splitStringTotal $$
CREATE FUNCTION get_splitStringTotal 
(f_string varchar(400), f_delimiter varchar(5)) 
RETURNS INT
RETURN (1+LENGTH(f_string)-LENGTH(REPLACE(f_string,f_delimiter,'')))$$ 

--创建函数(获取字符串指定位置的分割结果)
DROP function IF EXISTS get_splitString $$
CREATE FUNCTION get_splitString
(f_string varchar(400), f_delimiter varchar(5), f_order int) 
RETURNS varchar(50)  
BEGIN 
declare result varchar(255) default ''; 
set result = reverse(substring_index(reverse(substring_index(f_string,f_delimiter,f_order)),f_delimiter,1));
return result; 
END $$ 

--创建函数(分割字符串，将结果插入临时表)
DROP function IF EXISTS splitString $$ 
CREATE function splitString
(f_string varchar(400), f_delimiter varchar(5)) 
returns int
begin
    declare cnt int default 0; 
    declare i int default 0;
	SET cnt = get_splitStringTotal(f_string, f_delimiter);
    WHILE i<cnt
    do 
    set i = i + 1; 
    insert into tmp_genres(genre) values (get_splitString(f_string, f_delimiter, i)); 
end while; 
return 1;
END $$

-- 生成结果
DELIMITER ;
truncate tmp_genres;
select splitString(genres,'|') from movie;
select count(distinct t.genre) from tmp_genres t;
```

##### 一共有多少电影没有外部链接

```
select count(distinct t.moviedid)
from link t
where t.imdbid is null and t.tmbdid id null;
```

##### 2018年一共有多少人进行过电影评分

```
select count(distinct t.userid)
from rating t
where 
t.timestamp>=TIMESTAMPDIFF(SECOND, '1970-01-01 00:00:00','2018-01-01 00:00:00')
and
t.timestamp<TIMESTAMPDIFF(SECOND, '1970-01-01 00:00:00','2019-01-01 00:00:00');
```

##### 2018年评分5分以上的电影及其对应的标签

```
select 
    t1.movieid
    ,t1.rating
    ,t2.tag
from
	(select 
		t.movieid as movieid, 
		avg(t.rating) as rating
	from rating t
	where 
		t.timestamp>=TIMESTAMPDIFF(SECOND, '1970-01-01 00:00:00','2018-01-01 00:00:00')
	and
		t.timestamp<TIMESTAMPDIFF(SECOND, '1970-01-01 00:00:00','2019-01-01 00:00:00')
	group by t.movieid) t1
left join
	(select 
		t.movieid as movieid, 
		group_concat(distinct tag separator '|')  as tag
	from tag t
	where
		t.timestamp>=TIMESTAMPDIFF(SECOND, '1970-01-01 00:00:00','2018-01-01 00:00:00')
	and
		t.timestamp<TIMESTAMPDIFF(SECOND, '1970-01-01 00:00:00','2019-01-01 00:00:00')
	group by t.movieid) t2
on t1.movieid=t2.movieid
where t1.rating>=5
order by t1.rating desc, t1.movieid asc;
```

