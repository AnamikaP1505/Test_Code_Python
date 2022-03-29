import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

filepath='data.csv'
df=spark.read.option("header",true).csv(filepath)

df.show()
val df1= df.withColumn("SalePrice",(col("Quantity") * col("UnitPrice")))
df1.show()

df1.groupBy('CustomerID').agg(sum("Quantity").as("Total_Quantity"),sum("SalePrice").as("Total_SalePrice")).show(false)

