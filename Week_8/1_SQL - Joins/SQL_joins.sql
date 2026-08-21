--****17-08-2026 . SQL - Joins****
-- ============================================================
-- 1. CUSTOMERS TABLE
-- ============================================================
SELECT current_database();
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    gender VARCHAR(10),
    city VARCHAR(50),
    phone BIGINT,
    join_date DATE
);

-- Insert customer data

INSERT INTO customers
(customer_id, customer_name, gender, city, phone, join_date)
VALUES
(101, 'Rahul Sharma', 'Male', 'Hyderabad', 9876543210, '2024-01-10'),
(102, 'Sneha Reddy', 'Female', 'Bangalore', 9876543211, '2024-02-15'),
(103, 'Arjun Kumar', 'Male', 'Chennai', 9876543212, '2024-02-20'),
(104, 'Priya Singh', 'Female', 'Mumbai', 9876543213, '2024-01-25'),
(105, 'Kiran Rao', 'Male', 'Pune', 9876543214, '2024-04-05');

INSERT INTO customers
(customer_id, customer_name, gender, city, phone, join_date)
VALUES
(106, 'Anjali Verma', 'Female', 'Delhi', 9876543215, '2024-05-10'),
(107, 'Ravi Kumar', 'Male', 'Hyderabad', 9876543216, '2024-06-15'),
(108, 'Pooja Reddy', 'Female', 'Chennai', 9876543217, '2024-07-20'),
(109, 'Vikram Singh', 'Male', 'Pune', 9876543218, '2024-08-05'),
(110, 'Deepika Rao', 'Female', 'Mumbai', 9876543219, '2024-09-12');

SELECT *
FROM customers
ORDER BY customer_id;
-- ============================================================
-- 2. ORDERS TABLE
-- ============================================================
DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    store_id INT,
    order_date DATE,
    payment_method VARCHAR(20)
);

-- Insert order data

INSERT INTO orders
(order_id, customer_id, store_id, order_date, payment_method)
VALUES
(5001, 101, 1, '2025-01-10', 'UPI'),
(5002, 102, 2, '2025-01-11', 'Card'),
(5003, 103, 3, '2025-01-12', 'Cash'),
(5004, 104, 4, '2025-01-13', 'UPI'),
(5005, 105, 1, '2025-01-14', 'Card');

INSERT INTO orders
(order_id, customer_id, store_id, order_date, payment_method)
VALUES
(5006, 106, 2, '2025-01-15', 'UPI'),
(5007, 107, 3, '2025-01-16', 'Cash'),
(5008, 999, 4, '2025-01-17', 'Card');


SELECT *
FROM orders
ORDER BY order_id;

-- Check orders

SELECT * FROM orders;

-- ============================================================
-- 3. ORDER_ITEMS TABLE
-- ============================================================

DROP TABLE IF EXISTS order_items;

CREATE TABLE order_items (
    item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT
);

-- Insert order item data
-- Values are taken from the order_items screenshot

INSERT INTO order_items
(item_id, order_id, product_id, quantity)
VALUES
(1, 1001, 101, 1),
(2, 1001, 103, 2),
(3, 1002, 102, 1),
(4, 1003, 105, 3),
(5, 1004, 104, 2),
(6, 1005, 106, 1),
(7, 1006, 108, 1),
(8, 1007, 109, 2),
(9, 1008, 110, 1),
(10, 1009, 107, 1);

-- Check order_items

SELECT * FROM order_items;

-- ============================================================
-- 4. PRODUCTS TABLE
-- ============================================================

DROP TABLE IF EXISTS products;

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    brand VARCHAR(50),
    price DECIMAL(10,2)
);


-- Insert product data

INSERT INTO products
(product_id, product_name, category, brand, price)
VALUES
(1001, 'Phone 15', 'Mobiles', 'Apple', 80000.00),
(1002, 'Galaxy S24', 'Mobiles', 'Samsung', 70000.00),
(1003, 'Dell Laptop', 'Electronics', 'Dell', 65000.00),
(1004, 'Nike Shoes', 'Footwear', 'Nike', 5000.00),
(1005, 'Levis Jeans', 'Clothing', 'Levis', 2500.00);


-- Check products

SELECT * FROM products;


-- ============================================================
-- 5. STORES TABLE
-- ============================================================

DROP TABLE IF EXISTS stores;

CREATE TABLE stores (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(100),
    city VARCHAR(50),
    manager_name VARCHAR(100)
);


-- Insert store data

INSERT INTO stores
(store_id, store_name, city, manager_name)
VALUES
(1, 'Mega Mart Hyderabad', 'Hyderabad', 'Ramesh'),
(2, 'Super Store Bangalore', 'Bangalore', 'Anitha'),
(3, 'City Retail Chennai', 'Chennai', 'Vikram'),
(4, 'Smart Bazaar Mumbai', 'Mumbai', 'Pooja');


-- Check stores

SELECT * FROM stores;

--joins
--INNER JOIN
select c.customer_name , o.payment_method 
from customers c 
join orders o on c.customer_id = o.customer_id;

--LEFT JOIN
select c.customer_name , o.payment_method 
from customers c
left join orders o on c.customer_id  = o.customer_id;

--RIGHT JOIN
select c.customer_name , o.payment_method 
from customers c 
right join orders o on c.customer_id = o.customer_id 

select c.customer_name , o.payment_method , oi.quantity 
from customers c 
join orders o on c.customer_id = o.customer_id 
join order_items oi on o.order_id = oi.order_id;


DELETE FROM order_items;

select * from order_items;

INSERT INTO order_items
(item_id, order_id, product_id, quantity)
VALUES
(1, 5001, 1001, 1),
(2, 5001, 1003, 2),
(3, 5002, 1002, 1),
(4, 5003, 1005, 3),
(5, 5004, 1004, 2),
(6, 5005, 1001, 1),
(7, 5006, 1003, 1),
(8, 5007, 1002, 2);

--TWO TABLES JOIN
SELECT
    c.customer_name,
    o.payment_method,
    oi.quantity
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id;

--TWO TABLES JOIN
SELECT
    c.customer_name,
    o.payment_method,
    oi.quantity
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id;

--THREE TABLES JOIN
SELECT
    c.customer_name,
    o.payment_method,
    oi.quantity,
    p.product_name
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON p.product_id = oi.product_id;

--THREE TABLES JOIN CASE
SELECT
    c.customer_name,
    o.payment_method,
    oi.quantity,
    p.product_name,
case
	when oi.quantity = 1 then 'low quantity'
	when oi.quantity = 2 then 'moderate'
	else 'high' end status
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON p.product_id = oi.product_id;

--***TASK **ON** *p*.product\_id = *oi*.product\_id;  group by on these four columns and having, where clause***
--basic query

SELECT
    c.customer_name,
    o.payment_method,
    oi.quantity,
    p.product_name,
    CASE
        WHEN oi.quantity = 1 THEN 'low quantity'
        WHEN oi.quantity = 2 THEN 'moderate'
        ELSE 'high'
    END AS status
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON p.product_id = oi.product_id;

--Add WHERE
SELECT
    c.customer_name,
    o.payment_method,
    oi.quantity,
    p.product_name,
    CASE
        WHEN oi.quantity = 1 THEN 'low quantity'
        WHEN oi.quantity = 2 THEN 'moderate'
        ELSE 'high'
    END AS status
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON p.product_id = oi.product_id
WHERE oi.quantity >= 2;

--GROUP BY
SELECT
    c.customer_name,
    o.payment_method,
    oi.quantity,
    p.product_name,
    CASE
        WHEN oi.quantity = 1 THEN 'low quantity'
        WHEN oi.quantity = 2 THEN 'moderate'
        ELSE 'high'
    END AS status
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON p.product_id = oi.product_id
GROUP BY
    c.customer_name,
    o.payment_method,
    oi.quantity,
    p.product_name;

--Add WHERE + GROUP BY
SELECT
    c.customer_name,
    o.payment_method,
    oi.quantity,
    p.product_name,
    CASE
        WHEN oi.quantity = 1 THEN 'low quantity'
        WHEN oi.quantity = 2 THEN 'moderate'
        ELSE 'high'
    END AS status
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON p.product_id = oi.product_id
WHERE oi.quantity > 1
GROUP BY
    c.customer_name,
    o.payment_method,
    oi.quantity,
    p.product_name;

--Now understand HAVING

SELECT
    p.product_name,
    SUM(oi.quantity) AS total_quantity
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON p.product_id = oi.product_id
GROUP BY
    p.product_name
HAVING SUM(oi.quantity) > 2;

--Use all three together
SELECT
    p.product_name,
    SUM(oi.quantity) AS total_quantity
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON p.product_id = oi.product_id
WHERE oi.quantity > 1
GROUP BY
    p.product_name
HAVING SUM(oi.quantity) > 2;

--Your four-column version with WHERE + HAVING
SELECT
    c.customer_name,
    o.payment_method,
    oi.quantity,
    p.product_name,
    CASE
        WHEN oi.quantity = 1 THEN 'low quantity'
        WHEN oi.quantity = 2 THEN 'moderate'
        ELSE 'high'
    END AS status,
    SUM(oi.quantity) AS total_quantity
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON p.product_id = oi.product_id
WHERE oi.quantity >= 1
GROUP BY
    c.customer_name,
    o.payment_method,
    oi.quantity,
    p.product_name
HAVING SUM(oi.quantity) >= 2;
--OUTER JOIN
select * 
from customers c 
left join orders o on c.customer_id = o.customer_id 
union
select * 
from customers c 
right join orders o on c.customer_id = o.customer_id

select * 
from customers c 
left join orders o on c.customer_id = o.customer_id 
union all
select * 
from customers c 
right join orders o on c.customer_id = o.customer_id

--CROSS JOIN
--select * 
--from customers c 
--left join orders o on c.customer_id = o.customer_id 
--union all
--select * 
--from customers c 
--cross join orders o on c.customer_id = o.customer_id

--NATURAL JOIN
select * 
from customers c 
join orders o on c.customer_id  = o.customer_id;

select * 
from customers c 
natural join orders o;

--*****REAL TIME EXAMPLE*****
SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.payment_method
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id;

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.payment_method
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
ORDER BY c.customer_id;

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.payment_method
FROM customers c
RIGHT JOIN orders o
    ON c.customer_id = o.customer_id
ORDER BY o.order_id;

--self join
CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    designation VARCHAR(50),
    salary DECIMAL(10,2),
    manager_id INT
);

INSERT INTO employee VALUES
(101, 'Rahul', 'CEO', 150000, NULL),
(102, 'Sneha', 'Manager', 90000, 101),
(103, 'Arjun', 'Team Lead', 70000, 102),
(104, 'Priya', 'Developer', 50000, 103),
(105, 'Kiran', 'Developer', 48000, 103),
(106, 'Anjali', 'HR', 45000, 102);

SELECT *
FROM employee;

select emp.emp_name employee, mng.emp_name manager, emp.salary as emp_salary, mng.salary manager_salary
from employee emp
join employee mng
on emp.manager_id = mng.emp_id
