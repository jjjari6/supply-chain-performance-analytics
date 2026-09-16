import pandas as pd

# -----------------------------------
# 1. LOAD CLEANED DATA
# -----------------------------------

file_path = "data/cleaned/DataCoSupplyChainDataset_cleaned.csv"

df = pd.read_csv(
    file_path,
    parse_dates=[
        "order_date_dateorders",
        "shipping_date_dateorders"
    ]
)


# -----------------------------------
# 2. OVERALL KPI SUMMARY
# -----------------------------------

total_orders = df["order_id"].nunique()
total_sales = df["sales"].sum()
total_profit = df["benefit_per_order"].sum()

late_delivery_rate = (
    df["late_delivery_risk"].mean() * 100
)

avg_shipping_days = df["days_for_shipping_real"].mean()

print("\n===== OVERALL KPIS =====")
print(f"Total Orders: {total_orders:,}")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Late Delivery Rate: {late_delivery_rate:.2f}%")
print(f"Average Actual Shipping Days: {avg_shipping_days:.2f}")


# -----------------------------------
# 3. DELIVERY STATUS ANALYSIS
# -----------------------------------

delivery_status = (
    df["delivery_status"]
    .value_counts()
    .reset_index()
)

delivery_status.columns = [
    "delivery_status",
    "order_count"
]

print("\n===== DELIVERY STATUS =====")
print(delivery_status)


# -----------------------------------
# 4. SHIPPING MODE PERFORMANCE
# -----------------------------------

shipping_mode = (
    df.groupby("shipping_mode")
    .agg(
        orders=("order_id", "nunique"),
        avg_actual_shipping_days=("days_for_shipping_real", "mean"),
        avg_scheduled_shipping_days=("days_for_shipment_scheduled", "mean"),
        late_delivery_rate=("late_delivery_risk", "mean")
    )
    .reset_index()
)

shipping_mode["late_delivery_rate"] *= 100

shipping_mode = shipping_mode.sort_values(
    "late_delivery_rate",
    ascending=False
)

print("\n===== SHIPPING MODE PERFORMANCE =====")
print(shipping_mode.round(2))


# -----------------------------------
# 5. CATEGORY PERFORMANCE
# -----------------------------------

category_performance = (
    df.groupby("category_name")
    .agg(
        sales=("sales", "sum"),
        profit=("benefit_per_order", "sum"),
        orders=("order_id", "nunique")
    )
    .reset_index()
)

category_performance["profit_margin_pct"] = (
    category_performance["profit"]
    / category_performance["sales"]
    * 100
)

category_performance = category_performance.sort_values(
    "sales",
    ascending=False
)

print("\n===== TOP 10 CATEGORIES BY SALES =====")
print(category_performance.head(10).round(2))


# -----------------------------------
# 6. MARKET PERFORMANCE
# -----------------------------------

market_performance = (
    df.groupby("market")
    .agg(
        sales=("sales", "sum"),
        profit=("benefit_per_order", "sum"),
        orders=("order_id", "nunique")
    )
    .reset_index()
)

market_performance["profit_margin_pct"] = (
    market_performance["profit"]
    / market_performance["sales"]
    * 100
)

market_performance = market_performance.sort_values(
    "sales",
    ascending=False
)

print("\n===== MARKET PERFORMANCE =====")
print(market_performance.round(2))


# -----------------------------------
# 7. MOST PROFITABLE PRODUCTS
# -----------------------------------

product_performance = (
    df.groupby("product_name")
    .agg(
        sales=("sales", "sum"),
        profit=("benefit_per_order", "sum"),
        quantity=("order_item_quantity", "sum")
    )
    .reset_index()
)

product_performance = product_performance.sort_values(
    "profit",
    ascending=False
)

print("\n===== TOP 10 PRODUCTS BY PROFIT =====")
print(product_performance.head(10).round(2))


# -----------------------------------
# 8. LOSS-MAKING PRODUCTS
# -----------------------------------

loss_products = product_performance[
    product_performance["profit"] < 0
].sort_values("profit")

print("\n===== TOP 10 LOSS-MAKING PRODUCTS =====")
print(loss_products.head(10).round(2))


# -----------------------------------
# 9. EXPORT SUMMARY TABLES
# -----------------------------------

shipping_mode.to_csv(
    "data/cleaned/shipping_mode_performance.csv",
    index=False
)

category_performance.to_csv(
    "data/cleaned/category_performance.csv",
    index=False
)

market_performance.to_csv(
    "data/cleaned/market_performance.csv",
    index=False
)

product_performance.to_csv(
    "data/cleaned/product_performance.csv",
    index=False
)

print("\nAnalysis summary files exported successfully.")