select current_database();

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    gender VARCHAR(10)
);

INSERT INTO customers
(customer_id, customer_name, city, gender)
VALUES
(101, 'Rahul', 'Hyderabad', 'Male'),
(102, 'Priya', 'Chennai', 'Female'),
(103, 'Arjun', 'Bangalore', 'Male'),
(104, 'Sneha', 'Hyderabad', 'Female'),
(105, 'Kiran', 'Mumbai', 'Male');

SELECT *
FROM customers;

DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(50),
    category VARCHAR(50),
    quantity INT,
    amount DECIMAL(10,2),
    order_date DATE
);

INSERT INTO orders
(order_id, customer_id, product, category, quantity, amount, order_date)
VALUES
(1, 101, 'Laptop', 'Electronics', 1, 60000, '2026-01-10'),
(2, 102, 'Phone', 'Electronics', 1, 60000, '2026-01-12'),
(3, 101, 'Mouse', 'Accessories', 3, 1500, '2026-01-15'),
(4, 103, 'Laptop', 'Electronics', 1, 65000, '2026-01-20'),
(5, 104, 'Keyboard', 'Accessories', 2, 3000, '2026-02-05'),
(6, 105, 'Phone', 'Electronics', 1, 25000, '2026-02-10'),
(7, 102, 'Headphones', 'Accessories', 2, 5000, '2026-02-15'),
(8, 101, 'Monitor', 'Electronics', 1, 18000, '2026-02-28'),
(9, 103, 'Mouse', 'Accessories', 2, 1200, '2026-03-01'),
(10, 104, 'Phone', 'Electronics', 1, 30000, '2026-03-05');

SELECT *
FROM orders;

--***@@##20-08-2026 . SQL - CTE(Common Table Expressions)
select * from customers;

select * from orders;

--Syntax

--with cte_name as(
--cte query
--)

--select * from cte_name

select * from orders
where category = 'Electronics'

WITH electronics_orders AS (
    SELECT *
    FROM orders
    WHERE category = 'Electronics'
)
SELECT *
FROM electronics_orders;

WITH electronics_orders AS (
    SELECT *
    FROM orders
    WHERE category = 'Electronics'
)
SELECT *
FROM electronics_orders where product = 'Laptop';

select * from orders where category = 'Electronics' and product = 'Laptop';

WITH electronics_orders AS (
    SELECT *
    FROM orders
    WHERE category = 'Electronics'
)
SELECT product,
sum(quantity) FROM electronics_orders
group by 1;

WITH high_prods AS (
    SELECT *
    FROM orders
    WHERE amount>20000
)
select * from high_prods;

WITH cust_sales AS (
    SELECT customer_id, sum(Amount) as total_sales
    FROM orders
    group by 1
)
select * from cust_sales where total_sales >50000.00;

select * from orders;

WITH feb_data AS
(
    SELECT *
    FROM orders
    WHERE EXTRACT(MONTH FROM order_date) = 2
)
SELECT *
FROM feb_data;

with cus_order_details as
(
    select c.customer_name,
           c.city,
           c.gender,
           o.product,
           o.amount
    from customers c
    join orders o
        on c.customer_id = o.customer_id
)

select * from cus_order_details;

with cust_sales as
(
    select c.customer_name,
           c.gender,
           sum(o.amount * o.quantity) as total_sales
    from customers c
    join orders o
        on c.customer_id = o.customer_id
    group by 1, 2
)

select *
from cust_sales
where total_sales > 40000;

select * from customers;

select * from orders;

with cust_sales as
(
    select customer_id,
           sum(amount) as total_sales
    from orders
    group by 1
)

select customer_id,
       total_sales
from cust_sales;

with cust_sales as
(
    select customer_id,
           sum(amount) as total_sales
    from orders
    group by 1
),
cust_rank as
(
    select customer_id,
           total_sales,
           rank() over(order by total_sales desc) as sales_rnk
    from cust_sales
)

select *
from cust_rank;

WITH cust_sales AS
(
    SELECT customer_id,
           SUM(amount) AS total_sales
    FROM orders
    GROUP BY 1
),
cust_rank AS
(
    SELECT customer_id,
           total_sales,
           RANK() OVER (ORDER BY total_sales DESC) AS sales_rnk
    FROM cust_sales
)

SELECT c.customer_name,
       cr.total_sales,
       cr.sales_rnk
FROM customers c
JOIN cust_rank cr
    ON c.customer_id = cr.customer_id
ORDER BY cr.sales_rnk;