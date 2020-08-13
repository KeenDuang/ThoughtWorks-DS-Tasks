-- **数据库级别：**  
--  显示所有数据库  
show databases;
--  进入某个数据库  
use db_name;;
--  创建一个数据库  
create databse db_name；
--  创建指定字符集的数据库  
create database db_name default character set utf8 collate utf8_general_ci; /*utf8 */
create database db_name default character set gbk collate gbk_chinese_ci;   /*gbk */
--  显示数据库的创建信息   
show create database db_name;
--  修改数据库的编码  
alter database db_name character set utf8;
--  删除一个数据库   
drop database db_name;


-- **表级别**
--  修改表名
alter table ta rename tb                            /*把表名由ta修改为tb              */
--  修改字段的数据类型
alter table t1 modify name varchar(50);             /*修改表t1的name字段为varchar(50) */
--  修改字段名
alter table t1 change name myname varchar(15);      /*修改表t1的name字段为myname，也可以修改类型 */
--  添加字段
alter table t1 add lv int;                          /*表t1添加一个lv字段，定义字段类型，也可以添加约束 */
--  删除字段
alter table t1 drop lv;                             /*表t1删除lv字段                   */
--  修改表的存储引擎
alter table t1 engine=MyISAM;
--  删除表的外键约束
alter table t1 drop foreign key fk_name;            /*把t1表的外键约束fk_name删除       */
--  删除一张表
drop table t1;                                      /*删除t1表                          */