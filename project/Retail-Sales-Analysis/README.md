# 🛒 Retail Sales Analysis

## 📌 Project Overview

**Retail Sales Analysis** is a data analytics project that analyzes retail sales data using **Python, Pandas, NumPy, PostgreSQL, SQL, and Power BI**.

The project follows an end-to-end data analytics workflow:

```text
Python
   ↓
Pandas / NumPy
   ↓
Data Generation & Cleaning
   ↓
Excel / CSV
   ↓
PostgreSQL
   ↓
SQL Analysis
   ↓
Power BI
   ↓
Interactive Dashboard
```

---

## 🎯 Project Objectives

* Generate and prepare retail sales data
* Clean and validate the data using Pandas
* Store cleaned data in PostgreSQL
* Perform analysis using SQL
* Analyze sales by product, category, city, and region
* Connect PostgreSQL with Power BI
* Build an interactive retail sales dashboard
* Generate business insights from sales data

---

## 🛠️ Technologies Used

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Data processing              |
| Pandas     | Data cleaning and analysis   |
| NumPy      | Data generation              |
| Excel      | Data storage / preparation   |
| PostgreSQL | Database                     |
| SQL        | Data analysis                |
| SQLAlchemy | Python–PostgreSQL connection |
| Psycopg2   | PostgreSQL driver            |
| DBeaver    | Database management          |
| Power BI   | Dashboard and visualization  |

---

# 📁 Project Structure

```text
Retail-Sales-Analysis/
│
├── .venv/
│
├── data/
│   ├── raw/
│   │   └── retail_sales.xlsx
│   │
│   └── processed/
│       └── retail_sales_cleaned.csv
│
├── python/
│   ├── generate_data.py
│   └── data_cleaning.py
│
├── sql/
│   └── analysis_queries.sql
│
├── excel/
│   └── retail_sales_cleaned.xlsx
│
├── powerbi/
│   └── retail_sales_dashboard.pbix
│
├── database.py
├── models.py
├── create_tables.py
├── load_data.py
├── analysis.py
├── test_db.py
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

The retail sales dataset contains information such as:

```text
Order_ID
Order_Date
Customer
Gender
City
Region
Category
Product
Quantity
Unit_Price
Discount
Sales_Amount
```

### Example

| Order_ID | Customer | City      | Category    | Product | Quantity | Sales Amount |
| -------: | -------- | --------- | ----------- | ------- | -------: | -----------: |
|     1001 | Ramesh   | Hyderabad | Electronics | Laptop  |        2 |        90000 |
|     1002 | Anjali   | Bangalore | Grocery     | Oil     |        3 |         4500 |
|     1003 | Vijay    | Mumbai    | Furniture   | Chair   |        1 |        12000 |

---

# 🐍 Python Data Generation

`generate_data.py` is used to generate retail sales records.

```powershell
python python\generate_data.py
```

Generated data is stored in:

```text
data/raw/retail_sales.xlsx
```

---

# 🧹 Data Cleaning

`data_cleaning.py` performs basic data preparation:

* Remove duplicate records
* Remove missing values
* Convert date columns
* Convert numeric columns
* Calculate/validate sales amounts
* Export cleaned data

Run:

```powershell
python python\data_cleaning.py
```

Output:

```text
data/processed/retail_sales_cleaned.csv
```

---

# 🐘 PostgreSQL Database

Database:

```text
retail_db
```

PostgreSQL connection:

```python
DATABASE_URL = "postgresql://postgres:ramesh@localhost:5432/retail_db"
```

> Replace the password if your PostgreSQL password is different.

---

# 🗄️ Create Database Table

The project uses SQLAlchemy to create the `retail_sales` table.

Run:

```powershell
python create_tables.py
```

Table:

```text
retail_sales
```

Main columns:

```text
id
order_id
order_date
customer
gender
city
region
category
product
quantity
unit_price
discount
sales_amount
```

The `id` column is automatically generated:

```text
1
2
3
4
5
...
```

So it does not need to be manually entered.

---

# 📥 Load Data into PostgreSQL

After cleaning the data:

```powershell
python load_data.py
```

The flow is:

```text
retail_sales_cleaned.csv
          ↓
       Pandas
          ↓
     SQLAlchemy
          ↓
      PostgreSQL
          ↓
    retail_sales
```

---

# 🔍 Database Testing

To test the PostgreSQL connection:

```powershell
python test_db.py
```

Expected:

```text
Database connected successfully!
(1,)
```

---

# 🖥️ DBeaver

The database can be viewed and managed using DBeaver.

```text
PostgreSQL
    ↓
retail_db
    ↓
Schemas
    ↓
public
    ↓
Tables
    ↓
retail_sales
```

Check records:

```sql
SELECT *
FROM retail_sales
LIMIT 10;
```

Check total records:

```sql
SELECT COUNT(*)
FROM retail_sales;
```

---

# 📈 SQL Analysis

The project performs analysis such as:

### Total Sales

```sql
SELECT
    SUM(sales_amount) AS total_sales
FROM retail_sales;
```

### Total Orders

```sql
SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM retail_sales;
```

### Category-wise Sales

```sql
SELECT
    category,
    SUM(sales_amount) AS total_sales
FROM retail_sales
GROUP BY category
ORDER BY total_sales DESC;
```

### City-wise Sales

```sql
SELECT
    city,
    SUM(sales_amount) AS total_sales
FROM retail_sales
GROUP BY city
ORDER BY total_sales DESC;
```

### Region-wise Sales

```sql
SELECT
    region,
    SUM(sales_amount) AS total_sales
FROM retail_sales
GROUP BY region
ORDER BY total_sales DESC;
```

### Product-wise Sales

```sql
SELECT
    product,
    SUM(sales_amount) AS total_sales
FROM retail_sales
GROUP BY product
ORDER BY total_sales DESC;
```

---

# 📊 Power BI Dashboard

PostgreSQL is connected to Power BI.

### Connection

```text
Server: localhost
Port: 5432
Database: retail_db
```

Table:

```text
retail_sales
```

### Dashboard KPIs

```text
Total Sales
Total Orders
Total Quantity
```

### Visualizations

```text
Monthly Sales Trend
Category-wise Sales
Region-wise Sales
City-wise Sales
Product-wise Sales
```

Example dashboard layout:

```text
┌───────────────────────────────────────────────┐
│             RETAIL SALES DASHBOARD            │
├──────────────┬──────────────┬─────────────────┤
│ Total Sales  │ Total Orders │ Total Quantity  │
├──────────────┴──────────────┴─────────────────┤
│                                               │
│              Monthly Sales Trend              │
│                                               │
├──────────────────────┬────────────────────────┤
│ Category-wise Sales  │ Region-wise Sales      │
│                      │                        │
├──────────────────────┼────────────────────────┤
│ City-wise Sales      │ Product-wise Sales     │
│                      │                        │
└──────────────────────┴────────────────────────┘
```

---

# 🚀 How to Run the Project

## Step 1 — Activate Virtual Environment

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

You should see:

```text
(.venv)
```

---

## Step 2 — Install Packages

```powershell
pip install -r requirements.txt
```

---

## Step 3 — Test Database

```powershell
python test_db.py
```

---

## Step 4 — Create Table

```powershell
python create_tables.py
```

---

## Step 5 — Generate Data

```powershell
python python\generate_data.py
```

---

## Step 6 — Clean Data

```powershell
python python\data_cleaning.py
```

---

## Step 7 — Load Data

```powershell
python load_data.py
```

---

## Step 8 — Run Analysis

```powershell
python analysis.py
```

---

## Step 9 — Verify in DBeaver

```sql
SELECT COUNT(*)
FROM retail_sales;
```

Then:

```sql
SELECT *
FROM retail_sales
LIMIT 10;
```

---

# 🔄 Complete Project Flow

```text
                    RETAIL SALES ANALYSIS
                             │
                             ↓
                     Python / NumPy
                             │
                             ↓
                    Generate Sales Data
                             │
                             ↓
                          Excel
                             │
                             ↓
                         Pandas
                             │
                             ↓
                      Data Cleaning
                             │
                             ↓
                           CSV
                             │
                             ↓
                        SQLAlchemy
                             │
                             ↓
                       PostgreSQL
                             │
                             ↓
                        DBeaver
                             │
                             ↓
                       SQL Analysis
                             │
                             ↓
                         Power BI
                             │
                             ↓
                    Interactive Dashboard
```

---

# 💡 Business Questions

This project can answer questions such as:

1. What is the total sales amount?
2. How many orders were placed?
3. Which category generates the highest sales?
4. Which product performs best?
5. Which city has the highest sales?
6. Which region performs best?
7. What are the monthly sales trends?
8. Which customers generate high sales?
9. How does discount affect sales?
10. Which products/categories should receive more attention?

---

# 🎯 Key Learning Outcomes

Through this project, the following skills are demonstrated:

```text
Python
   ↓
Pandas
   ↓
NumPy
   ↓
Data Cleaning
   ↓
Excel / CSV
   ↓
PostgreSQL
   ↓
SQL
   ↓
DBeaver
   ↓
Power BI
   ↓
Data Visualization
```

---

# 👨‍💻 Author

**Ramesh**

### Skills Demonstrated

```text
Python
Pandas
NumPy
SQL
PostgreSQL
SQLAlchemy
DBeaver
Power BI
Data Analysis
Data Visualization
```

---

## ⭐ Project Summary

> **Retail Sales Analysis is an end-to-end data analytics project where retail sales data is generated and prepared using Python, Pandas, and NumPy, stored and analyzed in PostgreSQL using SQL, validated through DBeaver, and finally connected to Power BI to create an interactive sales dashboard.**
