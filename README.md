<h1> Automated Retail Analytics Pipeline  </h1> 

## 📖 Project Overview

This project simulates an end-to-end automated analytics pipeline for a retail organization. 

The system extracts transactional sales data, performs data cleaning and transformation (ETL), stores structured data in a SQLite database, and generates automated KPI reports.

The objective is to demonstrate real-world data engineering and analytics workflow using Python and SQLite.


## 🏢 Business Problem

Retail managers manually generate daily and monthly sales reports from CSV files. This process is:

- Time-consuming
- Error-prone
- Not scalable

The company requires an automated system to:
- Clean raw sales data
- Store it centrally
- Generate KPI metrics
- Support faster decision-making



## 🏗️ System Architecture

Raw CSV Data  
      ↓  
Data Cleaning & Transformation (Python)  
      ↓  
SQLite Data Warehouse  
      ↓  
Analytics & KPI Computation  
      ↓  
Automated Reporting


## 📂 Data Source

Dataset: Online Retail Dataset  
Type: Transaction-level sales data  

Key Columns:
- InvoiceNo
- StockCode
- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country



## 🔄 ETL Process

### Extract
- Load CSV file using pandas

### Transform
- Remove duplicate rows
- Remove cancelled orders (negative quantities)
- Handle missing CustomerID
- Create new column: TotalPrice = Quantity × UnitPrice
- Convert InvoiceDate to datetime format

### Load
- Store cleaned data into SQLite database


## 🗄️ Storage Design

SQLite was selected because:
- Lightweight and serverless
- Suitable for academic projects
- Easy integration with Python

The database follows a simplified star-schema design.

## ⏰ Scheduling

The ETL process is designed to run automatically using scheduled execution (simulated cron-based scheduling).

Future improvement includes integration with Apache Airflow.


## 📊 Logging & Monitoring

- Python logging module is used to track pipeline execution.
- Logs include:
  - Start time
  - End time
  - Number of rows processed
  - Error handling



## 📈 Reporting Layer

The system generates:
- Daily revenue
- Monthly revenue
- Top 10 products
- Sales by country
- Repeat customer analysis



## 🛠️ Tools & Technologies

- Python
- Pandas
- SQLite
- Jupyter Notebook
- Git & GitHub



## ▶️ How to Run

1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Run ETL script
5. Launch analytics notebook



## 🚀 Future Improvements

- Integration with Apache Airflow
- Deployment on cloud
- Real-time streaming data
- Interactive dashboard using Streamlit
  
