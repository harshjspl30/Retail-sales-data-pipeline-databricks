# Retail-sales-data-pipeline-databricks
End-to-End Retail Sales Data Pipeline using Databricks, PySpark, Spark SQL and Delta Lake

# Retail Sales Data Pipeline using Databricks

## Overview

This project demonstrates an end-to-end retail sales data pipeline built using Databricks, PySpark, Spark SQL, Delta Lake, and Unity Catalog.

## Architecture

Bronze → Silver → Gold Lakehouse Architecture

## Technologies

- Databricks
- PySpark
- Spark SQL
- Delta Lake
- Unity Catalog

## Layers

### Bronze Layer

Raw retail sales data loaded into Delta table.

### Silver Layer

- Data cleansing
- Remove duplicates
- Age Group creation
- Sales Year and Month derivation

### Gold Layer

- Product Revenue
- Monthly Revenue
- Customer Revenue

## Dashboard

Revenue and customer analytics dashboard built using the Gold Layer Data in Databricks SQL.

## Author

Harsh Kumar Gupta
