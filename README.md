# Supply Chain Performance Analytics

## Project Overview

This project analyzes supply chain and order fulfillment data to identify delivery inefficiencies, sales trends, profitability patterns, and regional performance.

Using **Python, SQL, SQLite, and Power BI**, I transformed a raw supply chain dataset containing more than 180,000 records into a cleaned analytical dataset, performed business-focused analysis, and developed an interactive Power BI dashboard.

---

## Business Questions

The analysis focuses on answering the following questions:

- How frequently are orders delivered late?
- Which shipping modes have the highest late-delivery rates?
- How do actual shipping times compare with scheduled shipping times?
- Which markets generate the most sales and profit?
- Which product categories generate the most revenue?
- Which products generate losses?
- Which geographic regions perform best?
- How does sales performance change over time?

---

## Dataset

This project uses the **DataCo Smart Supply Chain** dataset.

### Original Dataset

- **180,519 rows**
- **53 columns**
- Order and customer information
- Product and category information
- Sales and profitability
- Markets and geographic regions
- Shipping modes
- Scheduled and actual shipping times
- Delivery status
- Late-delivery risk

Large raw and processed data files are excluded from the GitHub repository using `.gitignore`.

---

## Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data exploration, cleaning, and analysis |
| Pandas | Data manipulation and aggregation |
| SQLite | Relational database creation |
| SQL | Business analysis and querying |
| Power BI | Interactive dashboard and visualization |
| VS Code | Development environment |
| Git & GitHub | Version control and portfolio hosting |

---

## Data Cleaning

Python and Pandas were used to prepare the dataset for analysis.

Key cleaning steps included:

- Identified missing values across all columns
- Removed `Product Description`, which contained no usable data
- Removed `Order Zipcode`, which contained extensive missing data
- Handled remaining missing customer information
- Converted order and shipping dates into datetime format
- Standardized column names for Python and SQL
- Checked for duplicate records
- Exported a cleaned dataset for analysis

### Cleaning Results

**Before Cleaning:**  
180,519 rows × 53 columns

**After Cleaning:**  
180,519 rows × 51 columns

**Remaining Missing Values:** 0

**Duplicate Rows:** 0

---

## Key Performance Indicators

| KPI | Result |
|---|---:|
| Total Sales | $36.78M |
| Total Profit | $3.97M |
| Total Orders | 65,752 |
| Late Delivery Rate | 54.83% |
| Average Actual Shipping Time | 3.50 days |

---

## Key Findings

### Delivery Performance

Delivery performance emerged as one of the largest operational issues in the dataset.

- **54.83%** of records were associated with late deliveries.
- First Class had a **95.32% late-delivery rate**.
- Second Class had a **76.63% late-delivery rate**.
- Same Day had a **45.74% late-delivery rate**.
- Standard Class had the lowest rate among the four modes at **38.07%**.

The comparison between scheduled and actual shipping times indicates that faster shipping options frequently failed to meet their scheduled service levels.

---

## Market Performance

| Market | Sales | Profit |
|---|---:|---:|
| Europe | $10.87M | $1.17M |
| LATAM | $10.28M | $1.12M |
| Pacific Asia | $8.27M | $857.75K |
| USCA | $5.07M | $564.31K |
| Africa | $2.29M | $252.07K |

Europe generated the highest overall sales and profit, while USCA produced the highest profit margin among the markets analyzed at approximately **11.14%**.

---

## Category Performance

The highest-performing product categories by sales included:

1. Fishing — **$6.93M**
2. Cleats — **$4.43M**
3. Camping & Hiking — **$4.12M**
4. Cardio Equipment — **$3.69M**
5. Women's Apparel — **$3.15M**

The analysis demonstrates the importance of evaluating both revenue and profitability when assessing product performance.

---

## Loss Analysis

SQL and Python analysis identified products with negative aggregate profit.

These products represent opportunities for further investigation into:

- Pricing strategy
- Discount levels
- Fulfillment costs
- Product margins
- Inventory decisions

---

## SQL Analysis

A SQLite database containing **180,519 records** was created from the cleaned dataset.

SQL queries were developed to analyze:

- Total orders
- Total sales and profit
- Late-delivery rate
- Delivery status
- Shipping-mode performance
- Category performance
- Market performance
- Regional performance
- Product profitability
- Loss-making products

The SQL results were validated against the Python analysis.

---

## Power BI Dashboard

An interactive Power BI dashboard was developed to present the major findings.

### Dashboard Features

- Total Sales KPI
- Total Profit KPI
- Total Orders KPI
- Late Delivery Rate KPI
- Average Shipping Days KPI
- Delivery Status Breakdown
- Late Delivery Rate by Shipping Mode
- Actual vs. Scheduled Shipping Days
- Sales by Market
- Profit by Market
- Top 10 Categories by Sales
- Monthly Sales Trend
- Market filter
- Shipping Mode filter
- Product Category filter

The complete Power BI `.pbix` file is available in the `dashboard` folder.

---

## Business Recommendations

### Improve Expedited Shipping Performance

First Class and Second Class shipping show particularly high late-delivery rates. Fulfillment processes and shipping expectations for expedited services should be investigated to determine why actual performance frequently exceeds scheduled delivery times.

### Monitor Profitability Alongside Revenue

High sales do not automatically indicate optimal profitability. Product and market performance should be evaluated using both revenue and profit margins.

### Review Loss-Making Products

Products generating aggregate losses should be evaluated for pricing, discounts, fulfillment costs, and continued inventory investment.

### Prioritize High-Value Markets and Categories

Europe and LATAM represent the largest markets by sales, while categories such as Fishing, Cleats, and Camping & Hiking contribute significant revenue. These areas warrant continued monitoring for demand, fulfillment performance, and profitability.

---

## Project Workflow

```text
Raw Dataset
     |
     v
Python Data Exploration
     |
     v
Python Data Cleaning
     |
     v
Cleaned Dataset
     |
     +------------------+
     |                  |
     v                  v
SQLite Database      Python Analysis
     |
     v
SQL Analysis
     |
     +------------------+
                        |
                        v
                 Power BI Dashboard
```

---

## Project Structure

```text
supply-chain-project/
│
├── dashboard/
│   └── Supply_Chain_Analytics_Dashboard.pbix
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── docs/
│
├── images/
│
├── notebooks/
│   ├── 01_data_exploration.py
│   ├── 02_data_cleaning.py
│   ├── 03_supply_chain_analysis.py
│   ├── 04_create_database.py
│   └── 05_run_sql_analysis.py
│
├── sql/
│   └── 01_supply_chain_analysis.sql
│
├── .gitignore
└── README.md
```

---

## Skills Demonstrated

- Data cleaning and preprocessing
- Exploratory data analysis
- Business KPI development
- SQL querying
- Database creation
- Supply chain analytics
- Profitability analysis
- Data visualization
- Power BI dashboard development
- Business insight communication

---

## Author

**Jay Jariwala**

Business Analytics Portfolio Project