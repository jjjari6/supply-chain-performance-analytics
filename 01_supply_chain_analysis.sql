-- =====================================================
-- SUPPLY CHAIN & INVENTORY ANALYTICS
-- SQL BUSINESS ANALYSIS
-- =====================================================


-- 1. TOTAL NUMBER OF ORDERS
SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM supply_chain;


-- 2. TOTAL SALES AND PROFIT
SELECT
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(benefit_per_order), 2) AS total_profit
FROM supply_chain;


-- 3. LATE DELIVERY RATE
SELECT
    ROUND(AVG(late_delivery_risk) * 100, 2)
        AS late_delivery_rate_pct
FROM supply_chain;


-- 4. DELIVERY STATUS BREAKDOWN
SELECT
    delivery_status,
    COUNT(*) AS order_items
FROM supply_chain
GROUP BY delivery_status
ORDER BY order_items DESC;


-- 5. SHIPPING MODE PERFORMANCE
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


-- 6. TOP 10 CATEGORIES BY SALES
SELECT
    category_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(benefit_per_order), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders
FROM supply_chain
GROUP BY category_name
ORDER BY total_sales DESC
LIMIT 10;


-- 7. MARKET PERFORMANCE
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


-- 8. TOP 10 PRODUCTS BY PROFIT
SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(benefit_per_order), 2) AS total_profit,
    SUM(order_item_quantity) AS quantity_sold
FROM supply_chain
GROUP BY product_name
ORDER BY total_profit DESC
LIMIT 10;


-- 9. LOSS-MAKING PRODUCTS
SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(benefit_per_order), 2) AS total_profit
FROM supply_chain
GROUP BY product_name
HAVING SUM(benefit_per_order) < 0
ORDER BY total_profit ASC;


-- 10. SALES AND PROFIT BY REGION
SELECT
    order_region,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(benefit_per_order), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders
FROM supply_chain
GROUP BY order_region
ORDER BY total_sales DESC;