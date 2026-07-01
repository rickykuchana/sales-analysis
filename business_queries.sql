-- Task 02 business questions on the sales data

-- 1. Total revenue by region, highest first
SELECT region, SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;

-- 2. Number of orders per category
SELECT category, COUNT(*) AS order_count
FROM sales
GROUP BY category;

-- 3. High-value orders over $1000
SELECT * FROM sales
WHERE quantity * price > 1000;
