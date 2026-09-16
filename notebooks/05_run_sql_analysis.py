import sqlite3
import pandas as pd

# -----------------------------------
# 1. CONNECT TO DATABASE
# -----------------------------------

database_file = "data/supply_chain.db"

connection = sqlite3.connect(database_file)


# -----------------------------------
# 2. DEFINE SQL QUERIES
# -----------------------------------

queries = {
    "total_orders": """
        SELECT
            COUNT(DISTINCT order_id) AS total_orders
        FROM supply_chain;
    """,

    "sales_profit": """
        SELECT
            ROUND(SUM(sales), 2) AS total_sales,
            ROUND(SUM(benefit_per_order), 2) AS total_profit
        FROM supply_chain;
    """,

    "late_delivery_rate": """
        SELECT
            ROUND(AVG(late_delivery_risk) * 100, 2)
                AS late_delivery_rate_pct
        FROM supply_chain;
    """,

    "delivery_status": """
        SELECT
            delivery_status,
            COUNT(*) AS order_items
        FROM supply_chain
        GROUP BY delivery_status
        ORDER BY order_items DESC;
    """,

    "shipping_mode_performance": """
        SELECT
            shipping_mode,
            COUNT(DISTINCT order_id) AS total_orders,
            ROUND(AVG(days_for_shipping_real), 2)
                AS avg_actual_shipping_days,
            ROUND(AVG(days_for_shipment_scheduled), 2)
                AS avg_scheduled_shipping_days,
            ROUND(AVG(late_delivery_risk) * 100, 2)
                AS late_delivery_rate_pct
        FROM supply_chain
        GROUP BY shipping_mode
        ORDER BY late_delivery_rate_pct DESC;
    """,

    "top_categories": """
        SELECT
            category_name,
            ROUND(SUM(sales), 2) AS total_sales,
            ROUND(SUM(benefit_per_order), 2) AS total_profit,
            COUNT(DISTINCT order_id) AS total_orders
        FROM supply_chain
        GROUP BY category_name
        ORDER BY total_sales DESC
        LIMIT 10;
    """,

    "market_performance": """
        SELECT
            market,
            ROUND(SUM(sales), 2) AS total_sales,
            ROUND(SUM(benefit_per_order), 2) AS total_profit,
            COUNT(DISTINCT order_id) AS total_orders,
            ROUND(
                SUM(benefit_per_order) / SUM(sales) * 100,
                2
            ) AS profit_margin_pct
        FROM supply_chain
        GROUP BY market
        ORDER BY total_sales DESC;
    """,

    "top_products": """
        SELECT
            product_name,
            ROUND(SUM(sales), 2) AS total_sales,
            ROUND(SUM(benefit_per_order), 2) AS total_profit,
            SUM(order_item_quantity) AS quantity_sold
        FROM supply_chain
        GROUP BY product_name
        ORDER BY total_profit DESC
        LIMIT 10;
    """,

    "loss_products": """
        SELECT
            product_name,
            ROUND(SUM(sales), 2) AS total_sales,
            ROUND(SUM(benefit_per_order), 2) AS total_profit
        FROM supply_chain
        GROUP BY product_name
        HAVING SUM(benefit_per_order) < 0
        ORDER BY total_profit ASC;
    """,

    "regional_performance": """
        SELECT
            order_region,
            ROUND(SUM(sales), 2) AS total_sales,
            ROUND(SUM(benefit_per_order), 2) AS total_profit,
            COUNT(DISTINCT order_id) AS total_orders
        FROM supply_chain
        GROUP BY order_region
        ORDER BY total_sales DESC;
    """
}


# -----------------------------------
# 3. RUN AND DISPLAY QUERIES
# -----------------------------------

for name, query in queries.items():

    print(f"\n===== {name.upper()} =====")

    result = pd.read_sql_query(query, connection)

    print(result.to_string(index=False))


# -----------------------------------
# 4. CLOSE DATABASE CONNECTION
# -----------------------------------

connection.close()

print("\nSQL analysis completed successfully.")
