
-- =========================================
-- TOTAL SALES
-- =========================================

SELECT
    SUM(sales_amount) AS total_sales
FROM retail_sales;


-- =========================================
-- TOTAL ORDERS
-- =========================================

SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM retail_sales;


-- =========================================
-- TOTAL QUANTITY
-- =========================================

SELECT
    SUM(quantity) AS total_quantity
FROM retail_sales;


-- =========================================
-- CATEGORY-WISE SALES
-- =========================================

SELECT
    category,
    SUM(sales_amount) AS total_sales
FROM retail_sales
GROUP BY category
ORDER BY total_sales DESC;


-- =========================================
-- CITY-WISE SALES
-- =========================================

SELECT
    city,
    SUM(sales_amount) AS total_sales
FROM retail_sales
GROUP BY city
ORDER BY total_sales DESC;


-- =========================================
-- REGION-WISE SALES
-- =========================================

SELECT
    region,
    SUM(sales_amount) AS total_sales
FROM retail_sales
GROUP BY region
ORDER BY total_sales DESC;


-- =========================================
-- PRODUCT-WISE SALES
-- =========================================

SELECT
    product,
    SUM(sales_amount) AS total_sales
FROM retail_sales
GROUP BY product
ORDER BY total_sales DESC;


-- =========================================
-- MONTHLY SALES
-- =========================================

SELECT
    DATE_TRUNC(
        'month',
        order_date
    ) AS month,

    SUM(sales_amount) AS total_sales

FROM retail_sales

GROUP BY month

ORDER BY month;