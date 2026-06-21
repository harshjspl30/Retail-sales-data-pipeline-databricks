# Databricks notebook source
# MAGIC %md 
# MAGIC ##Retail Sales Data Pipeline using PySpark & Databricks

# COMMAND ----------

#Read Bronze Table

bronze_df=spark.table(
    "retail_sales_catalog.retail_sales.bronze_retail_sales"
)
display(bronze_df)

# COMMAND ----------

bronze_df.printSchema()

# COMMAND ----------

print("Total Records:",bronze_df.count())

# COMMAND ----------

#Check Null value in Broze table

from pyspark.sql.functions import*

null_check=bronze_df.select([count(when(col(c).isNull(),c)).alias(c)
                             for c in bronze_df.columns])
display(null_check)

# COMMAND ----------

total_records=bronze_df.count()

distinct_records=bronze_df.dropDuplicates().count()

print("Total Records:",total_records)
print("Distinct Records:",distinct_records)
print("Duplicate_Records Count: ",total_records-distinct_records)


# COMMAND ----------

print(bronze_df.columns)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Silver Layer

# COMMAND ----------

from pyspark.sql.functions import*

bronze_df=spark.table("retail_sales_catalog.retail_sales.bronze_retail_sales")



# COMMAND ----------

##Data Cleaning

silver_df=bronze_df.dropDuplicates()

# COMMAND ----------

from pyspark.sql.functions import*

silver_df=(
    silver_df
    .withColumnRenamed("Transaction ID","transaction_id")
    .withColumnRenamed("Customer ID","Customer_id")
    .withColumnRenamed("Product Category","Product_Category")
    .withColumnRenamed("Price per Unit","Price_Per_Unit")
    .withColumnRenamed("Total Amount","Total_Amount")
)

# COMMAND ----------

#Creating Business Columns - Derived Columns

silver_df=(
    silver_df
    .withColumn("Sales_year",year(col("Date")))
    .withColumn("Sales_month",month(col("Date")))
    .withColumn("Sales_day",dayofmonth(col("Date")))
)
display(silver_df)

# COMMAND ----------

#Create Age Group
silver_df=(
    silver_df
    .withColumn("Age_Group",
                when(col("Age")<18,"Young")
                .when(col("Age")<45,"Adult")
                .otherwise("Senior")
))
display(silver_df)

# COMMAND ----------

silver_df.printSchema()

# COMMAND ----------

silver_df.display()

# COMMAND ----------

spark.table(
    "retail_sales_catalog.retail_sales.silver_retail_sales"
).printSchema()

# COMMAND ----------

silver_df.write\
    .format("delta")\
    .mode("overwrite")\
    .option("overwriteSchema","true")\
    .saveAsTable("retail_sales_catalog.retail_sales.silver_retail_sales")

# COMMAND ----------

display(silver_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Gold Layer Table 1: Product Revenue
# MAGIC
# MAGIC

# COMMAND ----------

from pyspark.sql.functions import*

silver_df=spark.table("retail_sales_catalog.retail_sales.silver_retail_sales")

gold_product=(
    silver_df
    .groupBy("Product_Category")
    .agg(
        sum("Total_Amount").alias("Revenue")
    )
)

# COMMAND ----------

display(gold_product)

# COMMAND ----------

gold_product.write\
    .format("delta")\
        .mode("overwrite")\
            .option("overwriteSchema","true")\
                .saveAsTable("retail_sales_catalog.retail_sales.gold_product_revenue")

# COMMAND ----------

gold_product.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC # Gold Layer Table 2: Monthly Revenue

# COMMAND ----------

from pyspark.sql.functions import *
gold_monthly_revenue=(
    silver_df
    .withColumn("sales_year",year(col("Date")))
    .withColumn("Sales_month",month(col("Date")))
    .groupBy("Sales_year","Sales_month")
    .agg(
        sum("Total_Amount").alias("Monthly_Revenue")
    )
    .orderBy("Sales_year","Sales_month")
)
display(gold_monthly_revenue)

# COMMAND ----------

gold_monthly_revenue.write\
    .format("delta")\
        .mode("overwrite")\
            .option("overwriteSchema","true")\
                .saveAsTable("retail_sales_catalog.retail_sales.gold_product_monthly_revenue")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Gold Table 3: Top Customers

# COMMAND ----------

gold_customer=(
    silver_df
    .groupBy("Customer_id")
    .agg(
        sum("Total_Amount").alias("Revenue")
    )
    .orderBy(col("Revenue").desc())
)
display(gold_customer)

# COMMAND ----------

gold_customer.write\
    .format("delta")\
        .mode("overwrite")\
            .option("overwriteSchema","true")\
                .saveAsTable("retail_sales_catalog.retail_sales.gold_customer_revenue")