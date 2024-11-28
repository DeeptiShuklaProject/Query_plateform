query_salary_more_than_avg = {
        "Query 1: Subquery with WHERE": """
            SELECT first_name, last_name, salary
            FROM employees
            WHERE salary > (SELECT AVG(salary) FROM employees);
        """,
        "Query 2: Common Table Expression (CTE)": """
            WITH avg_salary_cte AS (
                SELECT AVG(salary) AS avg_salary FROM employees
            )
            SELECT first_name, last_name, salary
            FROM employees, avg_salary_cte
            WHERE salary > avg_salary_cte.avg_salary;
        """,
        "Query 3: Derived Table": """
            SELECT e.first_name, e.last_name, e.salary, avg_salary.avg_salary
            FROM employees e
            JOIN (SELECT AVG(salary) AS avg_salary FROM employees) avg_salary
            ON e.salary > avg_salary.avg_salary;
        """,
        "CTE Query": """
            WITH avg_salary_cte AS (
                SELECT AVG(salary) AS avg_salary FROM employees
            )
            SELECT first_name, last_name, salary, avg_salary_cte.avg_salary
            FROM employees, avg_salary_cte
            WHERE salary > avg_salary_cte.avg_salary;
        """,
        "CTE QUERY WITH DIFF":"""WITH cte_avg_salary AS (
	        SELECT AVG(salary) as avg_salary FROM Employees 
        )
        SELECT first_name,last_name,salary,avg_salary,salary-avg_salary as diff  FROM employees,cte_avg_salary WHERE salary > avg_salary 
        """
        # MYSQL SYNTAX NOT GOOD FOR SQL
        # "@SET Query": """
        #     SET @avg_salary = (SELECT AVG(salary) FROM employees);
        #     SELECT first_name, last_name, salary, @avg_salary AS avg_salary
        #     FROM employees
        #     WHERE salary > @avg_salary;
        # """        
    }