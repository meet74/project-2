# Databricks notebook source
print("Shreehari")

# COMMAND ----------

# MAGIC %run "./constants"

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------



df = spark.read.option("header",True).parquet(f'{base_url}/processed/retail')

# COMMAND ----------

display(df)

# COMMAND ----------

#Aggregate total sales by country
df_sales_by_country = df.groupBy("country").agg(sum("total_price").alias("total_sales"))
display(df_sales_by_country)

# COMMAND ----------

#Filter transactions with high quantities
df_high_quantity = df.filter(col("quantity") > 100)
display(df_high_quantity)

# COMMAND ----------

# Calculate average unit price by stock code
df_avg_price_by_stock = df.groupBy("stock_code").agg(round(avg("unit_price"), 2).alias("avg_unit_price"))

display(df_avg_price_by_stock)

# COMMAND ----------

# aggregated data to separate locations
df_sales_by_country.write.mode('overwrite').parquet(f"{raw_url}/transformation/aggregated/sales_by_country")
df_high_quantity.write.mode('overwrite').parquet(f"{raw_url}/transformation/filtered/high_quantity")
df_avg_price_by_stock.write.mode('overwrite').parquet(f"{raw_url}/transformation/aggregated/avg_price_by_stock")


# COMMAND ----------

# transformed data with partitioning by year and month
df.write.mode('overwrite').partitionBy("invoice_year", "invoice_month").parquet(f"f{raw_url}/transformation/cleaned_retail_data")

# COMMAND ----------


