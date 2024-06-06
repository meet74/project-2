# Databricks notebook source
print("Shreehari")

# COMMAND ----------

# MAGIC %run "./constants"

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

schema = StructType([
    StructField("InvoiceNo", IntegerType(), True),
    StructField("StockCode", IntegerType(), True),
    StructField("Description", StringType(), True),
    StructField("Quantity", IntegerType(), True),
    StructField("InvoiceDate", TimestampType(), True),
    StructField("UnitPrice", DoubleType(), True),
    StructField("CustomerID", IntegerType(), True),
    StructField("Country", StringType(), True)
])

retail_df = spark.read.option("header",True).schema(schema).csv(f'{base_url}/raw/online-retail')

# COMMAND ----------

display(retail_df)

# COMMAND ----------

updated_retail_column_name = retail_df.withColumnRenamed("InvoiceNo", "invoice_no") \
       .withColumnRenamed("StockCode", "stock_code") \
       .withColumnRenamed("Description", "description") \
       .withColumnRenamed("Quantity", "quantity") \
       .withColumnRenamed("InvoiceDate", "invoice_date") \
       .withColumnRenamed("UnitPrice", "unit_price") \
       .withColumnRenamed("CustomerID", "customer_id") \
       .withColumnRenamed("Country", "country")
display(updated_retail_column_name)

# COMMAND ----------

# Handle missing values
removed_missing_values = updated_retail_column_name.fillna({
    "invoice_no": 0,  
    "stock_code": 0, 
    "description": "No Description",  
    "quantity": 0,  
    "invoice_date": "1970-01-01",  
    "unit_price": 0.0, 
    "customer_id": 0,  
    "country": "Unknown" 
})

display(removed_missing_values)

# COMMAND ----------

# Quantity should be non-negative.
handle_quantity = removed_missing_values.withColumn("quantity", when(col("quantity") < 0, 0).otherwise(col("quantity")))

# UnitPrice should be non-negative.
consistent_data = handle_quantity.withColumn("unit_price", when(col("unit_price") < 0, 0.0).otherwise(col("unit_price")))

display(consistent_data)


# COMMAND ----------

# Calculate TotalPrice as Quantity * UnitPrice.
new_total_price_coloumn = consistent_data.withColumn("total_price", round(col("quantity") * col("unit_price")))

# Create a unique identifier for each transaction.
new_transaction_id_coloumn = new_total_price_coloumn.withColumn("transaction_id", concat(col("invoice_no"), lit("_"), col("stock_code")))

# Extract year and month from InvoiceDate for time-based analysis.
new_invoice_year_coloumn = new_transaction_id_coloumn.withColumn("invoice_year", expr("year(invoice_date)"))
new_invoice_month_coloumn = new_invoice_year_coloumn.withColumn("invoice_month", expr("month(invoice_date)"))

# Extract day of the week from InvoiceDate for weekday analysis.
new_invoice_dayofweek_coloumn = new_invoice_month_coloumn.withColumn("invoice_dayof_week", expr("date_format(invoice_date, 'E')"))

display(new_invoice_dayofweek_coloumn)

# COMMAND ----------

new_invoice_dayofweek_coloumn.write.mode('overwrite').parquet(f"{raw_url}/processed/retail")

# COMMAND ----------


