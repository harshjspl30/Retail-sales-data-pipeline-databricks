-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Retail Sales Analytics
-- MAGIC
-- MAGIC This notebook provides business insights using Gold Layer tables.
-- MAGIC
-- MAGIC ## Analytics Covered
-- MAGIC
-- MAGIC 1. Product Revenue Analysis
-- MAGIC 2. Monthly Revenue Trend
-- MAGIC 3. Top Customers
-- MAGIC 4. Customer Segmentation
-- MAGIC 5. Revenue Distribution

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### # Product Revenue Analysis

-- COMMAND ----------

select
product_category,
revenue
from retail_sales_catalog.retail_sales.gold_product_revenue
order by Revenue desc;

-- COMMAND ----------

-- MAGIC %python
-- MAGIC df=spark.sql("""
-- MAGIC     select
-- MAGIC product_category,
-- MAGIC revenue
-- MAGIC from retail_sales_catalog.retail_sales.gold_product_revenue
-- MAGIC order by Revenue desc
-- MAGIC """
-- MAGIC )
-- MAGIC display(df)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Monthly Revenue Trend - Revenue Trend Over Time

-- COMMAND ----------

select make_date(sales_year, sales_month,1)AS sales_date, Monthly_Revenue
from
retail_sales_catalog.retail_sales.gold_product_monthly_revenue
order by Sales_year,Sales_month;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Top 10 Customers- Who are our highest spending customers?

-- COMMAND ----------

SELECT
    Customer_id,
    Revenue
FROM retail_sales_catalog.retail_sales.gold_customer_revenue
ORDER BY Revenue DESC
LIMIT 10;

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC ## Which age group generates maximum revenue?

-- COMMAND ----------

SELECT
    Age_Group,
    SUM(Total_Amount) Revenue
FROM retail_sales_catalog.retail_sales.silver_retail_sales
GROUP BY Age_Group
ORDER BY Revenue DESC;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Gender Revenue Analysis

-- COMMAND ----------

SELECT
    Gender,
    SUM(Total_Amount) Revenue
FROM retail_sales_catalog.retail_sales.silver_retail_sales
GROUP BY Gender;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Most sold product category

-- COMMAND ----------

SELECT
    Product_Category,
    SUM(Quantity) Total_Quantity
FROM retail_sales_catalog.retail_sales.silver_retail_sales
GROUP BY Product_Category
ORDER BY Total_Quantity DESC;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Customer Ranking (Window Function)

-- COMMAND ----------

SELECT
    Customer_id,
    SUM(Total_Amount) Revenue,
    RANK() OVER(
        ORDER BY SUM(Total_Amount) DESC
    ) Customer_Rank
FROM retail_sales_catalog.retail_sales.silver_retail_sales
GROUP BY Customer_id;