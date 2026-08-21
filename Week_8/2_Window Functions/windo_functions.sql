
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary NUMERIC(10,2) NOT NULL,
    joining_date DATE NOT NULL
);

INSERT INTO employees
(employee_name, department, salary, joining_date)
VALUES
('Ramesh', 'IT', 60000, '2022-01-10'),
('Suresh', 'IT', 75000, '2021-05-15'),
('Mahesh', 'IT', 75000, '2023-03-20'),
('Anil', 'IT', 50000, '2024-07-01'),

('Priya', 'HR', 55000, '2022-02-12'),
('Divya', 'HR', 65000, '2021-08-18'),
('Kavya', 'HR', 65000, '2023-06-10'),
('Sneha', 'HR', 45000, '2024-01-25'),

('Arjun', 'Sales', 70000, '2022-04-05'),
('Rahul', 'Sales', 80000, '2021-09-12'),
('Vijay', 'Sales', 80000, '2023-02-15'),
('Kiran', 'Sales', 50000, '2024-05-20');

select * 
from employees
order by employee_id;

--Basic
select department, sum(salary)
from employees
group by 1;

--Advance
select department, sum(salary) as total_salary
from employees 
group by department;

select employee_id, department, sum(salary)
from employees
group by 1,2;

select department, sum(salary)
from employees
group by 1
order by sum(salary) desc;

select department, sum(salary)
from employees
group by 1
order by sum(salary) desc
limit 1;

--Windos fun()
select *,
sum(salary) over(partition by department) as total_salary
from employees;

select *,
sum(salary) over(partition by department order by salary desc) total_salary
from employees;

--#########################
select *,
sum(salary) over(partition by department order by salary desc
				range between unbounded preceding and unbounded following) total_salary
from employees;

--OR
select *,
sum(salary) over(partition by department) as total_salary
from employees
order by total_salary;
--#########################
select *,
max(salary) over(partition by department order by salary desc) as max_salary
from employees;

select *,
min(salary) over(partition by department order by salary desc) as min_salary
from employees;

select *,
min(salary) over(partition by department order by salary desc
				range between unbounded preceding and current row) as min_salary
from employees;

select *,
min(salary) over w min_salary,
max(salary) over w max_salary,
sum(salary) over w total_salary
from employees
window w as(partition by department order by salary
			range between unbounded preceding and unbounded following);

select *,
min(salary) over w min_salary,
max(salary) over w max_salary,
sum(salary) over w total_salary,
count(*) over w total_count
from employees
window w as(partition by department order by salary
			range between unbounded preceding and unbounded following);

select *,
row_number() over(partition by department order by salary desc) as row_numberr
from employees;

--==wrong approach==

--select *,
--row_number() over(partition by department order by salary desc) as row_numberr
--from employees
--where row_numberr = 2;

--==wrong approach==

--select *,
--row_number() over(partition by department order by salary desc) as row_numberr
--from employees
--having row_numberr = 2;

--Right approach sub query
select * from
(select *,
row_number() over(partition by department order by salary desc) as row_numberr
from employees) as x
where x.row_numberr = 2;

select * from
(select *,
row_number() over(partition by department order by salary desc) as row_numberr,
rank() over(partition by department order by salary desc) as rnk
from employees) as x
where x.row_numberr = 2;

select * from
(select *,
row_number() over(partition by department order by salary desc) as row_numberr,
rank() over(partition by department order by salary desc) as rnk,
dense_rank() over(partition by department order by salary desc) as drnk
from employees) as x
where rnk = 1;

select *,
lag(salary) over(partition by department order by salary desc) as previous_employee_record,
lead(salary) over(partition by department order by salary desc) as next_employee_record
from employees


CREATE TABLE product (
    product_id SERIAL PRIMARY KEY,
    product_category VARCHAR(50) NOT NULL,
    brand VARCHAR(50) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) NOT NULL
);

INSERT INTO product
(product_category, brand, product_name, price)
VALUES
-- Phone
('Phone', 'Apple', 'iPhone 12 Pro Max', 1300),
('Phone', 'Apple', 'iPhone 12 Pro', 1100),
('Phone', 'Apple', 'iPhone 12', 1000),
('Phone', 'Samsung', 'Galaxy Z Fold 3', 1800),
('Phone', 'Samsung', 'Galaxy Z Flip 3', 1000),
('Phone', 'Samsung', 'Galaxy Note 20', 1200),

-- Laptop
('Laptop', 'Dell', 'Dell Inspiron 15', 800),
('Laptop', 'HP', 'HP Pavilion 15', 900),
('Laptop', 'Lenovo', 'Lenovo IdeaPad 5', 750),
('Laptop', 'Apple', 'MacBook Air', 1200),
('Laptop', 'Asus', 'Asus VivoBook 15', 700),

-- TV
('TV', 'Samsung', 'Samsung 55 Inch 4K', 1500),
('TV', 'LG', 'LG 55 Inch OLED', 1800),
('TV', 'Sony', 'Sony Bravia 55 Inch', 1700),
('TV', 'Samsung', 'Samsung 65 Inch 4K', 2200),

-- Watch
('Watch', 'Apple', 'Apple Watch Series 9', 500),
('Watch', 'Samsung', 'Galaxy Watch 6', 350),
('Watch', 'Titan', 'Titan Smart Watch', 250),
('Watch', 'Noise', 'Noise ColorFit', 150);

select * from product;

select product_category,
sum(price) as product_wise_revenue
from product
group by product_category;

select *,
sum(price) over(partition by product_category) as product_wise_revenue
from product
order by product_wise_revenue desc;

select *,
sum(price) over(partition by product_name) as product_wise_name
from product
order by product_wise_name desc;