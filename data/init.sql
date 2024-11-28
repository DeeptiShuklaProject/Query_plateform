CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10, 2),
    hire_date DATE,
    job_title VARCHAR(50),
    manager_id INT,
    gender CHAR(1),
    performance_rating INT
);

INSERT INTO employees VALUES
(1, 'Alice', 'Johnson', 101, 80000, '2018-06-01', 'Software Engineer', 4, 'F', 4),
(2, 'Bob', 'Smith', 102, 75000, '2020-03-15', 'Data Analyst', 4, 'M', 3),
(3, 'Charlie', 'Williams', 101, 120000, '2015-10-10', 'Senior Software Engineer', NULL, 'M', 5),
(4, 'Diana', 'Brown', 103, 60000, '2021-07-01', 'HR Specialist', NULL, 'F', 3),
(5, 'Eve', 'Davis', 101, 90000, '2019-11-20', 'DevOps Engineer', 3, 'F', 4),
(6, 'Frank', 'Miller', 102, 65000, '2022-01-05', 'Business Analyst', 2, 'M', 2);


CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    location VARCHAR(50)
);

INSERT INTO departments VALUES
(101, 'Engineering', 'New York'),
(102, 'Data Science', 'San Francisco'),
(103, 'Human Resources', 'Austin'),
(104, 'Marketing', 'Los Angeles');



CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50),
    start_date DATE,
    end_date DATE,
    budget DECIMAL(10, 2),
    department_id INT
);

INSERT INTO projects VALUES
(201, 'Project Alpha', '2022-01-01', '2023-01-01', 500000, 101),
(202, 'Data Insights', '2021-06-01', '2022-06-01', 300000, 102),
(203, 'Recruitment Drive', '2023-01-01', '2023-12-31', 100000, 103),
(204, 'Social Media Campaign', '2022-03-01', '2022-12-01', 200000, 104);




CREATE TABLE employee_project (
    employee_id INT,
    project_id INT,
    hours_contributed INT,
    PRIMARY KEY (employee_id, project_id)
);

INSERT INTO employee_project VALUES
(1, 201, 120),
(2, 202, 90),
(3, 201, 150),
(4, 203, 80),
(5, 201, 130),
(6, 202, 70);


CREATE TABLE performance_reviews (
    review_id INT PRIMARY KEY,
    employee_id INT,
    review_date DATE,
    rating INT,
    comments TEXT
);

INSERT INTO performance_reviews VALUES
(1, 1, '2023-06-15', 4, 'Excellent team player and proactive.'),
(2, 2, '2023-06-20', 3, 'Good performance but needs to improve communication.'),
(3, 3, '2023-06-25', 5, 'Outstanding contributions to projects.'),
(4, 4, '2023-07-01', 3, 'Reliable but needs to enhance skillset.'),
(5, 5, '2023-07-05', 4, 'Consistent performer.'),
(6, 6, '2023-07-10', 2, 'Requires significant improvement.');


