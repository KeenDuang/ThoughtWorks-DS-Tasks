# Python基础知识训练

## PySpark基础练习

Spark是一个流行的分布式计算框架，不仅提供了scala/java/python/R的编程接口支持，还可以支持基于SQL的开发。
如果运行于hadoop之上，它可以有效利用hadoop分布式存储和资源调度的能力，从而实现上PB级别数据的高效处理和分析。

在这个练习中，我们将尝试编写一个基本的PySpark程序。

请编写PySpark程序实现`student_stat.py`中的函数，以实现：

1. 读取文件`student.csv`得到一个`DataFrame`对象
2. 增加一列`grade`，当：
    `score > 90`时，`grade`值为`well`
    `80 < score <= 90`时，`grade`值为`less well`
    `score <= 80`时，`grade`值为`not well`
3. 统计各个`grade`的人数
4. 运行`student_stat_test.py`中的测试并视情况修改代码使测试可以通过。
