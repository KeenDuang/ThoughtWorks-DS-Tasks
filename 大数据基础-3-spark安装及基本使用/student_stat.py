from pyspark import SparkContext 
from pyspark.sql import SQLContext
from pyspark.sql.types import *
import pyspark.sql.functions as F
from pyspark.sql.functions import col

sc = SparkContext()
spark = SQLContext(sc)

class GradeStat:

    def __init__(self, well_count, less_well_count, not_good_count):
        self.well_count = well_count
        self.less_well_count = less_well_count
        self.not_good_count = not_good_count


def student_grade_stat(data_file: str) -> GradeStat:

    student=spark.read.csv('/spark_test/student.csv',header=True,inferSchema=True)
    
    def get_level(value):
        if  value > 90: 
            return 'well'
        elif value > 80: 
            return 'less well'
        else:
            return 'not well'    
        
    udf_level_func = F.udf(get_level, StringType())
    student_grade = student.withColumn("grade", udf_level_func("score"))
    student_stat = student_grade.groupby("grade").count()

    well_count = student_stat.filter(col("grade") == "well").collect()[0]['count']
    less_well_count = student_stat.filter(col("grade") == "less well").collect()[0]['count']
    not_good_count = student_stat.filter(col("grade") == "not well").collect()[0]['count']
    
    return GradeStat(well_count, less_well_count, not_good_count)
