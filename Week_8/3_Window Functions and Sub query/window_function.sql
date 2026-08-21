--#########19-08-2026 . SQL - Window Functions and Sub query
select * from product;

--first_value
select *,
first_value(brand) over(partition by product_category order by price desc) first_val
from product;

select *,
last_value(brand) over(partition by product_category order by price desc) last_val
from product;

select *,
last_value(brand) over(partition by product_category order by price desc
						rows between unbounded preceding and current row) last_val
from product;

select *,
last_value(brand) over(partition by product_category order by price desc
						rows between unbounded preceding and unbounded following) last_val
from product;

select *,
nth_value(product_name, 2) over(partition by product_category order by price desc
								rows between unbounded preceding and unbounded following) expensive_product
from product;

select *,
ntile(5) over(order by price desc)
from product;

select *,
case
	when x.bucketss = 1 then 'high products'
	when x.bucketss = 2 then 'moderate'
	else 'low' end status
from
(select *,
ntile(3) over(order by price desc) as bucketss
from product) x;

select * from
(select *,
case
	when x.bucketss = 1 then 'high products'
	when x.bucketss = 2 then 'moderate'
	else 'low' end status
from
(select *,
ntile(3) over(order by price desc) as bucketss
from product) x) z
where z.status = 'low';

--cumdist
select *,
cume_dist() over(order by price desc) cume_distt
from product;

select *,
cume_dist() over(order by price desc) cume_distt,
ROUND(
        (CUME_DIST() OVER (
            ORDER BY price DESC
        ) * 100)::numeric,
        2
    ) AS cume_dist_percentage
from product;

--percent rank
select *,
percent_rank() over(order by price desc) per_rankk,
ROUND(
        (CUME_DIST() OVER (
            ORDER BY price DESC
        ) * 100)::numeric,
        2
    ) AS per_rankk
from product;

--SUB QUERY
DROP TABLE IF EXISTS emp1;

CREATE TABLE emp1 (
    empno INT PRIMARY KEY,
    ename VARCHAR(100),
    job VARCHAR(50),
    mgr INT,
    hiredate DATE,
    sal DECIMAL(10,2),
    deptno INT
);


-- ============================================
-- INSERT VALUES
-- ============================================

INSERT INTO emp1
(empno, ename, job, mgr, hiredate, sal, deptno)
VALUES
(8009, 'BIPLAB', 'SALESMAN', 7698, '2022-03-12', 9000.00, 30),
(8010, 'Jason', 'SALESMAN', 7698, '2022-03-12', 9000.00, 30),
(7900, 'JAMES', 'CLERK', 7698, '1981-12-03', 805.00, 30),
(7698, 'BLAKE', 'MANAGER', 7839, '1981-05-01', 2850.00, 30),
(7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20', 1600.00, 30),
(7844, 'TURNER', 'SALESMAN', 7698, '1981-09-08', 1500.00, 30),
(7521, 'WARD', 'SALESMAN', 7698, '1981-02-22', 1250.00, 30),
(7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28', 1250.00, 30);


-- ============================================
-- CHECK DATA
-- ============================================

SELECT *
FROM emp1;

DROP TABLE IF EXISTS dept;

CREATE TABLE dept (
    deptno INT PRIMARY KEY,
    dname VARCHAR(50),
    loc VARCHAR(50)
);

INSERT INTO dept
(deptno, dname, loc)
VALUES
(10, 'ACCOUNTING', 'NEW YORK'),
(20, 'RESEARCH', 'DALLAS'),
(30, 'SALES', 'CHICAGO'),
(40, 'OPERATIONS', 'BOSTON');

SELECT * FROM dept;

--Step 1: First understand a normal/single query
SELECT deptno
FROM dept
WHERE dname = 'SALES';

SELECT *
FROM emp1
WHERE deptno = 30;

--Step 2: Convert two queries into one Subquery
SELECT *
FROM emp1
WHERE deptno = (
    SELECT deptno
    FROM dept
    WHERE dname = 'SALES'
);

--Step 3: Another very easy example

--Normal query
SELECT MAX(sal)
FROM emp1;

SELECT *
FROM emp1
WHERE sal = 9000;

--Convert into Subquery
SELECT *
FROM emp1
WHERE sal = (
    SELECT MAX(sal)
    FROM emp1
);

--Step 4: Average Salary
SELECT AVG(sal)
FROM emp1;

SELECT *
FROM emp1
WHERE sal > 4018.75;

--Now combine them:
SELECT *
FROM emp1
WHERE sal > (
    SELECT AVG(sal)
    FROM emp1
);

--Step 5: Minimum Salary
SELECT MIN(sal)
FROM emp1;

SELECT *
FROM emp1
WHERE sal = 805;

--Convert to one query:
SELECT *
FROM emp1
WHERE sal = (
    SELECT MIN(sal)
    FROM emp1
);

--Step 7: Greater Than Average
SELECT *
FROM emp1
WHERE sal > (
    SELECT AVG(sal)
    FROM emp1
);

--Step 8: Less Than Average

SELECT *
FROM emp1
WHERE sal < (
    SELECT AVG(sal)
    FROM emp1
);

