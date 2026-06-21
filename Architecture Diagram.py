# Databricks notebook source
# MAGIC %md
# MAGIC # Retail Sales Data Pipeline
# MAGIC
# MAGIC 📂 Retail Sales CSV
# MAGIC
# MAGIC ⬇️
# MAGIC
# MAGIC 🥉 Bronze Layer
# MAGIC - Raw Data
# MAGIC - Delta Table
# MAGIC - Load into the Catelog
# MAGIC
# MAGIC ⬇️
# MAGIC
# MAGIC 🥈 Silver Layer
# MAGIC - Data Cleansing
# MAGIC - Deduplication
# MAGIC - Transformations
# MAGIC
# MAGIC ⬇️
# MAGIC
# MAGIC 🥇 Gold Layer
# MAGIC - Revenue Metrics
# MAGIC - Customer Analytics
# MAGIC - Product Analytics
# MAGIC
# MAGIC ⬇️
# MAGIC
# MAGIC 📊 Dashboard / Reporting
# MAGIC - Spark SQL
# MAGIC - BI Reporting

# COMMAND ----------

# MAGIC %md
# MAGIC #Schema of Retail_Sales(Bronze Dataframe)
# MAGIC
# MAGIC ![image_1782038479398.png](./image_1782038479398.png "image_1782038479398.png")

# COMMAND ----------

# MAGIC %md
# MAGIC # Total Count of table and data in Bronze Layer: 
# MAGIC
# MAGIC ## Total Records: 1000

# COMMAND ----------

# MAGIC %md
# MAGIC ##How do you perform data quality validation in Spark?
# MAGIC
# MAGIC Ans: 
# MAGIC 1. Null Value Checks
# MAGIC
# MAGIC Identify missing or null values in critical columns.
# MAGIC Example: Customer ID, Transaction ID, Revenue.
# MAGIC
# MAGIC df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])
# MAGIC
# MAGIC 2. Duplicate Checks
# MAGIC
# MAGIC Find and remove duplicate records.
# MAGIC
# MAGIC df.dropDuplicates()
# MAGIC
# MAGIC 3. Data Type Validation
# MAGIC
# MAGIC Ensure columns have correct data types (Date, Integer, Decimal).
# MAGIC
# MAGIC df.printSchema()
# MAGIC
# MAGIC 4. Business Rule Validation
# MAGIC
# MAGIC Validate data against business rules.
# MAGIC Example:
# MAGIC Quantity > 0
# MAGIC Total Amount > 0
# MAGIC Age between 18 and 100
# MAGIC
# MAGIC 5. Referential Integrity Checks
# MAGIC
# MAGIC Verify matching records between fact and dimension tables using joins.
# MAGIC
# MAGIC 6. Record Count Validation
# MAGIC
# MAGIC Compare source and target record counts after processing.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Silver Layer --> Cleaned and Enriched Data

# COMMAND ----------

# MAGIC %md
# MAGIC # Gold Layer - Business KPIs / Metrics

# COMMAND ----------

# MAGIC %md
# MAGIC ## "How much revenue did each product category generate?"
# MAGIC
# MAGIC ![image_1782064651167.png](./image_1782064651167.png "image_1782064651167.png")
# MAGIC
# MAGIC