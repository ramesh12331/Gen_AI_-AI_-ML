DROP TABLE IF EXISTS retail_sales;

CREATE TABLE retail_sales (
    sale_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    country VARCHAR(50),
    sale_date DATE,
    category VARCHAR(50),
    product VARCHAR(50),
    quantity INT,
    unit_price DECIMAL(10,2),
    payment_method VARCHAR(50),
    sales_amount DECIMAL(10,2)
);

INSERT INTO retail_sales
(
    sale_id,
    customer_name,
    country,
    sale_date,
    category,
    product,
    quantity,
    unit_price,
    payment_method,
    sales_amount
)
VALUES
(1, 'Anwar_1', 'India', '2025-01-08', 'Clothing', 'T-Shirt', 2, 800.00, 'Card', 1600.00),

(2, 'Rahul_2', 'USA', '2025-01-15', 'Furniture', 'Chair', 3, 2500.00, 'Cash', 7500.00),

(3, 'Priya_3', 'UK', '2025-01-22', 'Groceries', 'Rice', 4, 500.00, 'Net Banking', 2000.00),

(4, 'Kiran_4', 'Canada', '2025-01-29', 'Beauty', 'Face Cream', 5, 700.00, 'UPI', 3500.00),

(5, 'Sneha_5', 'Australia', '2025-02-05', 'Sports', 'Football', 6, 1800.00, 'Card', 10800.00),

(6, 'John_6', 'Germany', '2025-02-12', 'Electronics', 'Laptop', 7, 55000.00, 'Cash', 385000.00),

(7, 'David_7', 'India', '2025-02-19', 'Clothing', 'T-Shirt', 8, 800.00, 'Net Banking', 6400.00),

(8, 'Maria_8', 'USA', '2025-02-26', 'Furniture', 'Chair', 9, 2500.00, 'UPI', 22500.00),

(9, 'Emma_9', 'UK', '2025-03-05', 'Groceries', 'Rice', 10, 500.00, 'Card', 5000.00),

(10, 'Mike_10', 'Canada', '2025-03-12', 'Beauty', 'Face Cream', 1, 700.00, 'Cash', 700.00),

(11, 'Anwar_11', 'Australia', '2025-03-19', 'Sports', 'Football', 2, 1800.00, 'Net Banking', 3600.00),

(12, 'Rahul_12', 'Germany', '2025-03-26', 'Electronics', 'Laptop', 3, 55000.00, 'UPI', 165000.00),

(13, 'Priya_13', 'India', '2025-04-02', 'Clothing', 'T-Shirt', 4, 800.00, 'Card', 3200.00),

(14, 'Kiran_14', 'USA', '2025-04-09', 'Furniture', 'Chair', 5, 2500.00, 'Cash', 12500.00),

(15, 'Sneha_15', 'UK', '2025-04-16', 'Groceries', 'Rice', 6, 500.00, 'Net Banking', 3000.00),

(16, 'John_16', 'Canada', '2025-04-23', 'Beauty', 'Face Cream', 7, 700.00, 'UPI', 4900.00),

(17, 'David_17', 'Australia', '2025-04-30', 'Sports', 'Football', 8, 1800.00, 'Card', 14400.00),

(18, 'Maria_18', 'Germany', '2025-05-07', 'Electronics', 'Laptop', 9, 55000.00, 'Cash', 495000.00),

(19, 'Emma_19', 'India', '2025-05-14', 'Clothing', 'T-Shirt', 10, 800.00, 'Net Banking', 8000.00),

(20, 'Mike_20', 'USA', '2025-05-21', 'Furniture', 'Chair', 1, 2500.00, 'UPI', 2500.00);
 
 
select * from retail_sales;

select country, sum(sales_amount) as total_amount
from retail_sales
group by 1
order by total_amount;

--select country, sum(sales_amount) as total_amount
--from retail_sales
--group by 1
--having total_amount > 100000;

SELECT country,
       SUM(sales_amount) AS total_amount
FROM retail_sales
GROUP BY country
HAVING SUM(sales_amount) > 100000;

SELECT country,
       COUNT(*) AS total_count
FROM retail_sales
GROUP BY country
HAVING COUNT(*) >= 4;

select category, round(avg(sales_amount),0) avggg
from retail_sales
group by 1
having avg(sales_amount)>5000;

select country, category, sum(sales_amount) total_amount
from retail_sales
group by 1,2;

select payment_method,
sum(sales_amount) as total_amount,
count(*) as trans
from retail_sales
group by 1
having count(*) >= 5
order by total_amount desc;

	---case expressions:
	
	select *,
	case 
		when quantity >=6 then 'high quantity prods'
		when quantity >=3 and quantity <=5 then 'moderate prods'
		else 'low quantity prods'
		end status
	from retail_sales;

