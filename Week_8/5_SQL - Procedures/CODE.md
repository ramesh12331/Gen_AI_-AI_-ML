# CREATE OR REPLACE – SQL Notes

## 1. Definition

`CREATE OR REPLACE` is used in **PostgreSQL** to create a database object if it does not exist, or replace/update its definition if it already exists.

It is commonly used with:

```sql
CREATE OR REPLACE FUNCTION
CREATE OR REPLACE PROCEDURE
CREATE OR REPLACE VIEW
```

### Simple Meaning

```text
CREATE OR REPLACE
        ↓
If object does not exist → CREATE
If object already exists → REPLACE its definition
```

---

# 2. Syntax

## Function Syntax

```sql
CREATE OR REPLACE FUNCTION function_name(
    parameters
)
RETURNS return_type
LANGUAGE plpgsql
AS $$
BEGIN

    -- SQL statements

    RETURN value;

END;
$$;
```

---

## Procedure Syntax

```sql
CREATE OR REPLACE PROCEDURE procedure_name(
    parameters
)
LANGUAGE plpgsql
AS $$
BEGIN

    -- SQL statements

END;
$$;
```

---

## View Syntax

```sql
CREATE OR REPLACE VIEW view_name AS
SELECT
    column1,
    column2
FROM table_name;
```

---

# 3. Example – Function

Suppose we have:

```sql
CREATE TABLE employee (
    emp_id INT,
    emp_name VARCHAR(100),
    dept_name VARCHAR(100),
    salary INT
);
```

### Create Function

```sql
CREATE OR REPLACE FUNCTION get_salary(
    p_emp_id INT
)
RETURNS INT
LANGUAGE plpgsql
AS $$
BEGIN

    RETURN (
        SELECT salary
        FROM employee
        WHERE emp_id = p_emp_id
    );

END;
$$;
```

### Execute Function

```sql
SELECT get_salary(103);
```

### Output

```text
4000
```

---

# 4. Example – Function Returning Table

If we want to get all employees from the IT department:

```sql
CREATE OR REPLACE FUNCTION it_department()
RETURNS TABLE (
    emp_id INT,
    emp_name VARCHAR(100),
    dept_name VARCHAR(100),
    salary INT
)
LANGUAGE plpgsql
AS $$
BEGIN

    RETURN QUERY
    SELECT
        e.emp_id,
        e.emp_name,
        e.dept_name,
        e.salary
    FROM employee e
    WHERE e.dept_name = 'IT';

END;
$$;
```

### Execute

```sql
SELECT *
FROM it_department();
```

### Output

```text
emp_id    emp_name    dept_name    salary
------    ---------   ----------   ------
103       Akbar       IT           4000
109       Sanjay      IT           6500
```

---

# 5. Example – Procedure

A procedure can be used to update an employee's salary.

```sql
CREATE OR REPLACE PROCEDURE update_employee_salary(
    p_emp_id INT,
    p_salary INT
)
LANGUAGE plpgsql
AS $$
BEGIN

    UPDATE employee
    SET salary = p_salary
    WHERE emp_id = p_emp_id;

END;
$$;
```

### Execute Procedure

```sql
CALL update_employee_salary(103, 6000);
```

### Check Result

```sql
SELECT *
FROM employee
WHERE emp_id = 103;
```

---

# 6. Example – View

A view can store a query for HR employees.

```sql
CREATE OR REPLACE VIEW hr_employees AS
SELECT
    emp_id,
    emp_name,
    dept_name,
    salary
FROM employee
WHERE dept_name = 'HR';
```

### Use View

```sql
SELECT *
FROM hr_employees;
```

---

# 7. `CREATE` vs `CREATE OR REPLACE`

### CREATE

```sql
CREATE FUNCTION test()
...
```

If the function already exists:

```text
ERROR
```

---

### CREATE OR REPLACE

```sql
CREATE OR REPLACE FUNCTION test()
...
```

If the function already exists:

```text
Existing definition
        ↓
Replace definition
```

---

# 8. `CREATE OR REPLACE` vs `DROP`

### DROP

```sql
DROP FUNCTION IF EXISTS test();
```

This **deletes** the function.

### CREATE OR REPLACE

```sql
CREATE OR REPLACE FUNCTION test()
...
```

This **keeps the object and replaces its definition**.

### Easy Difference

```text
DROP
 ↓
DELETE OBJECT

CREATE OR REPLACE
 ↓
CREATE / UPDATE OBJECT
```

---

# 9. Important Keywords

### `LANGUAGE plpgsql`

```sql
LANGUAGE plpgsql
```

Tells PostgreSQL that the function/procedure is written using **PL/pgSQL**.

---

### `AS $$`

```sql
AS $$
```

Starts the function/procedure body.

---

### `BEGIN`

```sql
BEGIN
```

Starts the block of SQL statements.

---

### `END`

```sql
END;
```

Ends the block.

---

### `$$`

```sql
$$;
```

Ends the function/procedure body.

---

# 10. `RETURN` vs `RETURN QUERY`

## RETURN

Used to return a **single value**.

```sql
RETURN 6000;
```

Example:

```sql
CREATE OR REPLACE FUNCTION get_salary()
RETURNS INT
LANGUAGE plpgsql
AS $$
BEGIN

    RETURN 6000;

END;
$$;
```

Call:

```sql
SELECT get_salary();
```

---

## RETURN QUERY

Used to return **rows from a SELECT query**.

```sql
RETURN QUERY
SELECT *
FROM employee;
```

Example:

```sql
CREATE OR REPLACE FUNCTION get_it_employees()
RETURNS TABLE (
    emp_id INT,
    emp_name VARCHAR(100),
    dept_name VARCHAR(100),
    salary INT
)
LANGUAGE plpgsql
AS $$
BEGIN

    RETURN QUERY
    SELECT
        emp_id,
        emp_name,
        dept_name,
        salary
    FROM employee
    WHERE dept_name = 'IT';

END;
$$;
```

Call:

```sql
SELECT *
FROM get_it_employees();
```

---

# 11. Function vs Procedure

```text
FUNCTION
   ↓
Returns something
   ↓
SELECT function_name();


PROCEDURE
   ↓
Performs an operation
   ↓
CALL procedure_name();
```

### Example

```sql
-- FUNCTION
CREATE OR REPLACE FUNCTION get_salary()
RETURNS INT
...


-- PROCEDURE
CREATE OR REPLACE PROCEDURE update_salary()
...
```

Execute:

```sql
-- Function
SELECT get_salary();

-- Procedure
CALL update_salary();
```

---

# 12. Tricks to Remember ⭐

### Trick 1

```text
CREATE OR REPLACE
        ↓
CREATE + UPDATE
```

If it doesn't exist → **CREATE**

If it exists → **REPLACE**

---

### Trick 2

Remember:

```text
FUNCTION  → RETURN
PROCEDURE → ACTION
```

---

### Trick 3

Remember how to execute:

```text
FUNCTION
   ↓
SELECT

PROCEDURE
   ↓
CALL
```

```sql
SELECT it_department();

CALL update_employee_salary(103, 6000);
```

---

### Trick 4

Remember `RETURN QUERY`:

```text
RETURN
       ↓
Single value

RETURN QUERY
       ↓
Multiple rows / SELECT result
```

---

### Trick 5 – PostgreSQL Structure

Remember this pattern:

```sql
CREATE OR REPLACE FUNCTION
        ↓
RETURNS
        ↓
LANGUAGE plpgsql
        ↓
AS $$
        ↓
BEGIN
        ↓
SQL LOGIC
        ↓
END;
        ↓
$$;
```

---

# 13. One-Minute Revision

```text
CREATE OR REPLACE
-----------------

Definition:
Used to create an object if it does not exist,
or replace its definition if it already exists.

Commonly used with:
1. FUNCTION
2. PROCEDURE
3. VIEW

FUNCTION:
Returns a value/result.

Execute:
SELECT function_name();

PROCEDURE:
Performs an operation.

Execute:
CALL procedure_name();

RETURN:
Returns a value.

RETURN QUERY:
Returns rows/result of a SELECT query.

LANGUAGE plpgsql:
Specifies PostgreSQL procedural language.

AS $$ ... $$:
Contains the function/procedure body.
```

## ⭐ Interview Answer

```text
Q: What is CREATE OR REPLACE?

A:
CREATE OR REPLACE is a PostgreSQL command used to
create a database object if it does not exist and
replace its existing definition if it already exists.
It is commonly used with functions, procedures, and views.
```
