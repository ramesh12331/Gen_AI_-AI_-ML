DROP TABLE IF EXISTS employee;

CREATE TABLE employee (
    emp_id INT,
    emp_name VARCHAR(100),
    dept_name VARCHAR(100),
    salary INT
);

INSERT INTO employee
(emp_id, emp_name, dept_name, salary)
VALUES
(105, 'Rohit', 'HR', 3000),
(102, 'Rajkumar', 'Human resources', 3000),
(103, 'Akbar', 'IT', 4000),
(104, 'Dorwin', 'Finance', 6500),
(105, 'Rohit', 'HR', 3000),
(106, 'Rajesh', 'Finance', 5000),
(107, 'Preet', 'HR', 7000),
(108, 'Maryam', 'Admin', 4000),
(109, 'Sanjay', 'IT', 6500);

SELECT *
FROM employee;

select * from employee 
where dept_name = 'HR'

--NOT SUPPORT 

--delimiter//
--create procedure hr_department()
--begin
--	select * from employee 
--where dept_name = 'HR'
--end//
--delimiter;

CREATE OR REPLACE PROCEDURE hr_department()
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT *
    FROM employee
    WHERE dept_name = 'HR';
END;
$$;

SELECT *
FROM hr_department();


DROP PROCEDURE IF EXISTS it_department();

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
    SELECT e.emp_id,
           e.emp_name,
           e.dept_name,
           e.salary
    FROM employee e
    WHERE e.dept_name = 'IT';
END;
$$;

SELECT *
FROM it_department();

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

CALL update_employee_salary(103, 6000);

SELECT *
FROM employee
WHERE emp_id = 103;
