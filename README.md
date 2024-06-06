# Project 2: Retail Inventory Management and Sales Forecasting

## Project Title
Retail Inventory Management and Sales Forecasting

## Project Description
This project aims to optimize inventory management and sales forecasting for a retail company. The process involves data ingestion, processing, storage, and analysis of various data sources such as sales transactions, inventory logs, and customer data to provide insights for better decision-making.

## Steps Followed and Observations
**Data Ingestion:**
   - Ingested data from sales transactions, inventory logs, and customer data using Azure Data Factory.
   - Stored raw data in Azure Data Lake Storage (ADLS) Gen2.

**Data Storage:**
   - Raw data was stored in ADLS Gen2, and processed data was stored in Azure Synapse Analytics for efficient querying and analysis.

**Data Transformation:**
   - Used PySpark in Azure Databricks to clean and transform the data.
   - Handled missing values, corrected inconsistencies, and performed feature engineering.

**Data Warehousing:**
   - Loaded transformed data into Azure Synapse Analytics.
   - Created external tables to reference the data stored in ADLS for optimized access.

**Data Analysis:**
   - Executed SQL queries in Synapse Analytics to perform data analysis.
   - Visualized insights using Power BI.


## Data Pipeline Process
- **Data Ingestion:** Ingested data from various sources using ADF.
- **Data Storage:** Stored raw and processed data in ADLS and Synapse Analytics.
- **Data Transformation:** Cleaned and transformed data using PySpark in Databricks.
- **Data Warehousing:** Loaded transformed data into Synapse Analytics and created external tables.
- **Data Analysis:** Performed SQL queries and visualized insights in Power BI.

## Transformation and Analytics Results
- **Total Sales by Country:** Bar charts showing total sales for each country.
- **High Quantity Transactions:** Tables listing high quantity transactions.
- **Average Unit Price by Stock Code:** Line charts showing average unit prices.
- **Monthly Sales Analysis:** Area charts showing monthly sales trends.
- **Top Selling Products:** Horizontal bar charts showing top selling products.
- **Customer Purchase Patterns:** Pie charts showing customer spending distribution.

## Conclusion
The project successfully optimized inventory management and sales forecasting for the retail company, providing valuable insights to support better decision-making. The use of Azure services ensured scalability, efficiency, and effective data visualization.


