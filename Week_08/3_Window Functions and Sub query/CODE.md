Yes 👍 For a **beginner**, the best way is to learn **Single Query → Subquery** step by step. Don't start with `ANY`, `ALL`, `EXISTS`, etc.

Let's use your `emp1` and `dept` tables.

# SQL Subquery — Beginner Method

## Step 1: First understand a normal/single query

Suppose you want employees from the **SALES** department.

First, find the department number:

```sql
SELECT deptno
FROM dept
WHERE dname = 'SALES';
```

Result:

```text
30
```

Now use that result in another query:

```sql
SELECT *
FROM emp1
WHERE deptno = 30;
```

This is **two separate queries**.

Think:

```text
Query 1
   ↓
Find SALES department number
   ↓
30
   ↓
Query 2
   ↓
Find employees where deptno = 30
```

---

# Step 2: Convert two queries into one Subquery

Instead of manually writing `30`:

```sql
SELECT *
FROM emp1
WHERE deptno = (
    SELECT deptno
    FROM dept
    WHERE dname = 'SALES'
);
```

Now you have:

```text
        OUTER QUERY
            ↓
SELECT * FROM emp1
WHERE deptno =
            ↓
       INNER QUERY
            ↓
SELECT deptno FROM dept
WHERE dname = 'SALES'
```

### ⭐ This is the basic meaning of Subquery

> **One query inside another query.**

---

# Step 3: Another very easy example

### Normal query

Suppose you want the employee with the **highest salary**.

First:

```sql
SELECT MAX(sal)
FROM emp1;
```

Result:

```text
9000
```

Then:

```sql
SELECT *
FROM emp1
WHERE sal = 9000;
```

Two queries.

---

## Convert into Subquery

```sql
SELECT *
FROM emp1
WHERE sal = (
    SELECT MAX(sal)
    FROM emp1
);
```

### Dry Run

First PostgreSQL executes the inner query:

```sql
SELECT MAX(sal)
FROM emp1;
```

Result:

```text
9000
```

Then the outer query becomes:

```sql
SELECT *
FROM emp1
WHERE sal = 9000;
```

So the result is:

```text
BIPLAB    9000
Jason     9000
```

---

# Step 4: Average Salary

First do it separately.

### Query 1

```sql
SELECT AVG(sal)
FROM emp1;
```

Suppose result:

```text
4018.75
```

### Query 2

```sql
SELECT *
FROM emp1
WHERE sal > 4018.75;
```

Now combine them:

```sql
SELECT *
FROM emp1
WHERE sal > (
    SELECT AVG(sal)
    FROM emp1
);
```

### Dry Run

```text
INNER QUERY
     ↓
AVG(sal)
     ↓
4018.75
     ↓
OUTER QUERY
     ↓
sal > 4018.75
```

---

# Step 5: Minimum Salary

First:

```sql
SELECT MIN(sal)
FROM emp1;
```

Then:

```sql
SELECT *
FROM emp1
WHERE sal = 805;
```

Convert to one query:

```sql
SELECT *
FROM emp1
WHERE sal = (
    SELECT MIN(sal)
    FROM emp1
);
```

---

# Step 6: Maximum Salary

```sql
SELECT *
FROM emp1
WHERE sal = (
    SELECT MAX(sal)
    FROM emp1
);
```

---

# Step 7: Greater Than Average

```sql
SELECT *
FROM emp1
WHERE sal > (
    SELECT AVG(sal)
    FROM emp1
);
```

Meaning:

> Show employees whose salary is greater than the average salary.

---

# Step 8: Less Than Average

```sql
SELECT *
FROM emp1
WHERE sal < (
    SELECT AVG(sal)
    FROM emp1
);
```

Meaning:

> Show employees whose salary is less than the average salary.

---

# 🧠 The Most Important Pattern

For now, memorize this pattern:

```sql
SELECT columns
FROM table
WHERE column OPERATOR
(
    SELECT value
    FROM table
    WHERE condition
);
```

Examples:

```text
=     → equal
>     → greater than
<     → less than
>=    → greater than or equal
<=    → less than or equal
```

For example:

```sql
WHERE sal > (
    SELECT AVG(sal)
    FROM emp1
);
```

---

# ⭐ Single Query → Subquery Learning Pattern

Always practice like this:

### 1️⃣ First query

```sql
SELECT MAX(sal)
FROM emp1;
```

### 2️⃣ Get the answer

```text
9000
```

### 3️⃣ Second query

```sql
SELECT *
FROM emp1
WHERE sal = 9000;
```

### 4️⃣ Combine

```sql
SELECT *
FROM emp1
WHERE sal = (
    SELECT MAX(sal)
    FROM emp1
);
```

That's the **best beginner approach**.

---

# 🔥 Practice These 5 First

Don't move to `EXISTS`, `ANY`, `ALL`, or correlated subqueries yet.

### Question 1

Find employees with the highest salary.

```sql
SELECT *
FROM emp1
WHERE sal = (
    SELECT MAX(sal)
    FROM emp1
);
```

### Question 2

Find employees with the lowest salary.

```sql
SELECT *
FROM emp1
WHERE sal = (
    SELECT MIN(sal)
    FROM emp1
);
```

### Question 3

Find employees earning more than average salary.

```sql
SELECT *
FROM emp1
WHERE sal > (
    SELECT AVG(sal)
    FROM emp1
);
```

### Question 4

Find employees earning less than average salary.

```sql
SELECT *
FROM emp1
WHERE sal < (
    SELECT AVG(sal)
    FROM emp1
);
```

### Question 5

Find employees working in SALES.

```sql
SELECT *
FROM emp1
WHERE deptno = (
    SELECT deptno
    FROM dept
    WHERE dname = 'SALES'
);
```

## 🧩 One-line memory trick

```text
FIRST → Write a normal query
SECOND → Get the result
THIRD → Put that query inside another query
FOURTH → That's a SUBQUERY
```

**For a beginner, this is the correct foundation:** `MAX → MIN → AVG → department lookup → then IN/EXISTS → then correlated subqueries.`
---

అవును 👍 మీరు ఇప్పుడు **SQL Subqueries** నేర్చుకుంటున్నారు. Screenshot‌లో ఉన్న `emp1` table ఆధారంగా **అన్ని important Subquery types** ని DBeaver + PostgreSQL కోసం step-by-step ఇస్తాను.

ముందుగా మనకు `emp1` తో పాటు `dept` table కూడా కావాలి.

# SQL SUBQUERIES — COMPLETE NOTES

## 1. What is a Subquery?

ఒక SQL query లోపల ఇంకొక SQL query ఉంటే దాన్ని **Subquery** అంటారు.

```sql
SELECT *
FROM emp1
WHERE deptno = (
    SELECT deptno
    FROM dept
    WHERE dname = 'SALES'
);
```

ఇక్కడ:

```text
Outer Query
     ↓
SELECT * FROM emp1
     ↓
Inner Query
     ↓
SELECT deptno FROM dept
WHERE dname = 'SALES'
```

**Simple memory:**

```text
Query inside Query = Subquery
```

---

# 2. Create `dept` Table

Screenshot‌లో `dept` table కూడా reference చేశారు. Practice కోసం:

```sql
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
```

---

# 3. Single-Row Subquery

## Definition

Subquery **only one row** return చేస్తే దాన్ని Single-Row Subquery అంటారు.

### Example

> Find employees working in SALES department.

```sql
SELECT *
FROM emp1
WHERE deptno = (
    SELECT deptno
    FROM dept
    WHERE dname = 'SALES'
);
```

### Dry Run

Inner query:

```sql
SELECT deptno
FROM dept
WHERE dname = 'SALES';
```

Result:

```text
30
```

Outer query becomes:

```sql
SELECT *
FROM emp1
WHERE deptno = 30;
```

Result:

```text
All employees from dept 30
```

### Important

`=` తో subquery ఉపయోగిస్తే subquery సాధారణంగా **one value** return చేయాలి.

---

# 4. Single-Row Subquery with `MAX()`

> Find employees earning the highest salary.

```sql
SELECT *
FROM emp1
WHERE sal = (
    SELECT MAX(sal)
    FROM emp1
);
```

### Dry Run

Inner query:

```sql
SELECT MAX(sal)
FROM emp1;
```

Result:

```text
9000
```

Outer query:

```sql
SELECT *
FROM emp1
WHERE sal = 9000;
```

Result:

```text
BIPLAB
Jason
```

Both have salary `9000`.

---

# 5. Single-Row Subquery with `MIN()`

> Find employee(s) earning the lowest salary.

```sql
SELECT *
FROM emp1
WHERE sal = (
    SELECT MIN(sal)
    FROM emp1
);
```

Result:

```text
JAMES
805
```

---

# 6. Greater Than Subquery

> Find employees earning more than the average salary.

```sql
SELECT *
FROM emp1
WHERE sal > (
    SELECT AVG(sal)
    FROM emp1
);
```

### Logic

```text
AVG salary
    ↓
Inner query
    ↓
Compare each employee salary
    ↓
sal > average
```

---

# 7. Less Than Subquery

> Find employees earning less than average salary.

```sql
SELECT *
FROM emp1
WHERE sal < (
    SELECT AVG(sal)
    FROM emp1
);
```

---

# 8. Subquery with `IN`

## Definition

`IN` is useful when the subquery returns **multiple values**.

Example:

> Find employees working in departments located in NEW YORK or DALLAS.

```sql
SELECT *
FROM emp1
WHERE deptno IN (
    SELECT deptno
    FROM dept
    WHERE loc IN ('NEW YORK', 'DALLAS')
);
```

Inner query may return:

```text
10
20
```

Outer query:

```sql
WHERE deptno IN (10, 20)
```

---

# 9. `IN` vs `=`

### `=`

Use when subquery returns one value:

```sql
WHERE deptno = (
    SELECT deptno
    FROM dept
    WHERE dname = 'SALES'
);
```

### `IN`

Use when subquery can return multiple values:

```sql
WHERE deptno IN (
    SELECT deptno
    FROM dept
);
```

### Memory Trick

```text
=   → ONE value

IN  → MULTIPLE values
```

---

# 10. `NOT IN`

> Find employees who are not working in departments 10 and 20.

```sql
SELECT *
FROM emp1
WHERE deptno NOT IN (
    SELECT deptno
    FROM dept
    WHERE deptno IN (10, 20)
);
```

Result will contain employees from other departments.

---

# 11. Subquery with `ANY`

`ANY` compares a value with **at least one value** returned by the subquery.

Example:

> Find employees whose salary is greater than ANY salary in the selected set.

```sql
SELECT *
FROM emp1
WHERE sal > ANY (
    SELECT sal
    FROM emp1
    WHERE deptno = 30
);
```

Think:

```text
sal > ANY
    ↓
Greater than at least one value
```

---

# 12. Subquery with `ALL`

`ALL` means the condition must be true for **every value** returned by the subquery.

Example:

> Find employees whose salary is greater than ALL salaries in department 30.

```sql
SELECT *
FROM emp1
WHERE sal > ALL (
    SELECT sal
    FROM emp1
    WHERE deptno = 30
);
```

Think:

```text
sal > ALL
    ↓
Greater than every value
```

### Easy Difference

```text
ANY
 ↓
At least one

ALL
 ↓
Every one
```

---

# 13. `EXISTS` Subquery

## Definition

`EXISTS` checks whether the subquery returns **at least one row**.

Example:

> Find employees whose department exists in the `dept` table.

```sql
SELECT *
FROM emp1 e
WHERE EXISTS (
    SELECT 1
    FROM dept d
    WHERE d.deptno = e.deptno
);
```

### Dry Run

For each employee:

```text
Employee deptno
      ↓
Check dept table
      ↓
Does matching department exist?
      ↓
YES → include employee
NO  → don't include employee
```

---

# 14. `NOT EXISTS`

> Find employees whose department does not exist in the department table.

```sql
SELECT *
FROM emp1 e
WHERE NOT EXISTS (
    SELECT 1
    FROM dept d
    WHERE d.deptno = e.deptno
);
```

This is the opposite of `EXISTS`.

```text
EXISTS
    ↓
Match exists

NOT EXISTS
    ↓
Match does not exist
```

---

# 15. Correlated Subquery ⭐

This is an important interview concept.

## Definition

A **Correlated Subquery** depends on the outer query.

The inner query refers to a column from the outer query.

### Example

> Find employees whose salary is greater than the average salary of their own department.

```sql
SELECT *
FROM emp1 e
WHERE sal > (
    SELECT AVG(e2.sal)
    FROM emp1 e2
    WHERE e2.deptno = e.deptno
);
```

Notice:

```sql
e.deptno
```

inside the subquery comes from the outer query.

That's why it is **correlated**.

### Dry Run

For each employee:

```text
Employee
   ↓
Find average salary of his department
   ↓
Compare employee salary
   ↓
Keep if salary > department average
```

### Memory Trick

```text
Normal Subquery
    ↓
Inner query can work independently

Correlated Subquery
    ↓
Inner query depends on outer query
```

---

# 16. Subquery in `SELECT`

A subquery can also appear inside the `SELECT` list.

Example:

```sql
SELECT
    e.empno,
    e.ename,
    e.sal,
    (
        SELECT AVG(e2.sal)
        FROM emp1 e2
    ) AS average_salary
FROM emp1 e;
```

Result concept:

```text
EMPNO | ENAME  | SAL    | AVERAGE_SALARY
------|--------|--------|---------------
8009  | BIPLAB | 9000   | ...
8010  | Jason  | 9000   | ...
...
```

The same overall average is displayed for each employee.

---

# 17. Subquery in `FROM`

A subquery inside `FROM` is called a **Derived Table** / inline view.

Example:

```sql
SELECT *
FROM (
    SELECT
        empno,
        ename,
        sal
    FROM emp1
    WHERE sal > 2000
) AS x;
```

Here:

```text
Inner Query
     ↓
Creates temporary result
     ↓
Outer Query
     ↓
Uses that result
```

### Important

In PostgreSQL, the subquery in `FROM` needs an alias:

```sql
) AS x
```

---

# 18. Subquery with `GROUP BY`

> Find departments whose average salary is greater than 2000.

```sql
SELECT deptno,
       AVG(sal) AS average_salary
FROM emp1
GROUP BY deptno
HAVING AVG(sal) > 2000;
```

This is actually `GROUP BY + HAVING`, not necessarily a subquery.

But we can use it as a subquery:

```sql
SELECT *
FROM emp1
WHERE deptno IN (
    SELECT deptno
    FROM emp1
    GROUP BY deptno
    HAVING AVG(sal) > 2000
);
```

### Logic

```text
GROUP BY
    ↓
Calculate department average
    ↓
HAVING
    ↓
Select qualifying departments
    ↓
Outer query finds employees
```

---

# 19. Subquery with `ORDER BY` and `LIMIT`

Your screenshot shows this type of practice.

> Find the employee with the highest salary.

```sql
SELECT *
FROM emp1
WHERE sal = (
    SELECT sal
    FROM emp1
    ORDER BY sal DESC
    LIMIT 1
);
```

Inner query:

```sql
SELECT sal
FROM emp1
ORDER BY sal DESC
LIMIT 1;
```

Result:

```text
9000
```

Outer query:

```sql
WHERE sal = 9000
```

---

# 20. Second Highest Salary ⭐

Very important interview question.

### Method 1 — `MAX()` Subquery

```sql
SELECT *
FROM emp1
WHERE sal = (
    SELECT MAX(sal)
    FROM emp1
    WHERE sal < (
        SELECT MAX(sal)
        FROM emp1
    )
);
```

### Easier PostgreSQL method

```sql
SELECT *
FROM emp1
ORDER BY sal DESC
OFFSET 1
LIMIT 1;
```

But for **subquery practice**, learn the first method.

---

# 21. Employees Earning More Than Manager

Because `emp1` has:

```text
empno
ename
mgr
sal
```

we can use a correlated/self-reference subquery.

```sql
SELECT *
FROM emp1 e
WHERE e.sal > (
    SELECT m.sal
    FROM emp1 m
    WHERE m.empno = e.mgr
);
```

### Relationship

```text
Employee
   ↓ mgr
Manager
   ↓
Manager salary
```

Then:

```text
Employee salary > Manager salary
```

---

# 22. Employee and Manager Names Using Subquery

```sql
SELECT
    e.empno,
    e.ename,
    (
        SELECT m.ename
        FROM emp1 m
        WHERE m.empno = e.mgr
    ) AS manager_name
FROM emp1 e;
```

Result concept:

```text
EMPNO | ENAME  | MANAGER_NAME
------|--------|-------------
8009  | BIPLAB | BLAKE
8010  | Jason  | BLAKE
7900  | JAMES  | BLAKE
7698  | BLAKE  | ...
```

This is a **correlated scalar subquery**.

---

# 23. Multiple-Column Subquery

PostgreSQL also supports comparing multiple columns.

Example:

```sql
SELECT *
FROM emp1
WHERE (deptno, sal) IN (
    SELECT deptno, MAX(sal)
    FROM emp1
    GROUP BY deptno
);
```

Meaning:

> Find the highest-paid employee(s) in each department.

The subquery returns pairs:

```text
deptno | max_salary
-------+-----------
30     | 9000
```

Then the outer query matches both:

```text
deptno
+
salary
```

---

# 24. Subquery vs JOIN

### Subquery

```sql
SELECT *
FROM emp1
WHERE deptno = (
    SELECT deptno
    FROM dept
    WHERE dname = 'SALES'
);
```

### JOIN

```sql
SELECT e.*
FROM emp1 e
JOIN dept d
    ON e.deptno = d.deptno
WHERE d.dname = 'SALES';
```

Both can solve the same problem.

### Beginner rule

Use subqueries when the problem naturally sounds like:

> "Find employees whose value is based on another query."

Use JOIN when you need to combine columns/data from multiple tables.

---

# 25. Complete Subquery Types — Cheat Sheet

| Type              | Main Idea                | Example                      |
| ----------------- | ------------------------ | ---------------------------- |
| Single-row        | Returns one row/value    | `= (SELECT...)`              |
| Multi-row         | Returns multiple rows    | `IN (SELECT...)`             |
| Scalar            | Returns one value        | `SELECT (SELECT AVG...)`     |
| `IN`              | Match any returned value | `IN (SELECT...)`             |
| `NOT IN`          | Exclude returned values  | `NOT IN (SELECT...)`         |
| `ANY`             | Match at least one       | `> ANY (...)`                |
| `ALL`             | Match every value        | `> ALL (...)`                |
| `EXISTS`          | At least one row exists  | `EXISTS (...)`               |
| `NOT EXISTS`      | No matching row          | `NOT EXISTS (...)`           |
| Correlated        | Depends on outer query   | `WHERE e.deptno = e2.deptno` |
| `FROM` subquery   | Derived table            | `FROM (SELECT...) x`         |
| `SELECT` subquery | Subquery in SELECT       | `(SELECT AVG(...))`          |

---

# 🎯 Most Important Interview Questions

### 1. What is a subquery?

A query written inside another query is called a subquery.

### 2. What is a single-row subquery?

A subquery that returns one row/value.

```sql
WHERE sal = (
    SELECT MAX(sal)
    FROM emp1
);
```

### 3. What is a multi-row subquery?

A subquery that returns multiple rows.

```sql
WHERE deptno IN (
    SELECT deptno
    FROM dept
);
```

### 4. Difference between `IN` and `EXISTS`?

```text
IN
 ↓
Compares values

EXISTS
 ↓
Checks whether rows exist
```

### 5. What is a correlated subquery?

A subquery that refers to a column from the outer query.

### 6. Difference between `ANY` and `ALL`?

```text
ANY → condition true for at least one value

ALL → condition true for every value
```

### 7. Can a subquery be used in `FROM`?

Yes.

```sql
SELECT *
FROM (
    SELECT *
    FROM emp1
) AS x;
```

### 8. Can a subquery be used in `SELECT`?

Yes.

```sql
SELECT
    ename,
    (SELECT AVG(sal) FROM emp1) AS avg_salary
FROM emp1;
```

---

# 🧠 Best Learning Order

Since you're learning SQL from beginner level, don't try to memorize all of them at once.

Learn in this order:

```text
1️⃣ What is Subquery?
       ↓
2️⃣ Single-row subquery
       ↓
3️⃣ MAX / MIN / AVG subqueries
       ↓
4️⃣ IN
       ↓
5️⃣ NOT IN
       ↓
6️⃣ ANY
       ↓
7️⃣ ALL
       ↓
8️⃣ EXISTS
       ↓
9️⃣ NOT EXISTS
       ↓
🔟 Correlated Subquery
       ↓
1️⃣1️⃣ Subquery in SELECT
       ↓
1️⃣2️⃣ Subquery in FROM
       ↓
1️⃣3️⃣ Multiple-column subquery
```

### ⭐ The 5 you should master first

```text
= (SELECT ...)
IN (SELECT ...)
EXISTS (SELECT ...)
> ANY (SELECT ...)
> ALL (SELECT ...)
```

Once these are clear, the remaining subquery types become much easier.
