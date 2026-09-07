DROP TABLE IF EXISTS retail_sales;


CREATE TABLE retail_sales (

    order_id INT PRIMARY KEY,

    order_date DATE,

    customer VARCHAR(100),

    gender VARCHAR(20),

    city VARCHAR(100),

    region VARCHAR(50),

    category VARCHAR(100),

    product VARCHAR(100),

    quantity INT,

    unit_price DECIMAL(12,2),

    discount DECIMAL(5,2),

    sales_amount DECIMAL(14,2)

);