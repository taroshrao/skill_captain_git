CREATE TABLE Employee (
  EmployeeID INT,
  EmployeeName VARCHAR(255),
  DepartmentID INT
);

CREATE TABLE Department (
  DepartmentID INT,
  DepartmentName VARCHAR(255)
);

-- 1. List of all possible combinations of employees and departments

select e.EmployeeID, e.EmployeeName, d.DepartmentID, d.DepartmentName
from Employee e
cross join Department d;

-- 2. List of employees who belong to at least one department

select distinct e.EmployeeName, d.DepartmentID
from employee e
inner join department d
on e.DepartmentID = d.DepartmentID;

--3. List of all employees and their department details, including employees without a department and departments without employees

SELECT e.EmployeeID, e.EmployeeName, d.DepartmentID, d.DepartmentName
FROM Employee e
LEFT JOIN Department d ON e.DepartmentID = d.DepartmentID

UNION

SELECT e.EmployeeID, e.EmployeeName, d.DepartmentID, d.DepartmentName
FROM Employee e
RIGHT JOIN Department d ON e.DepartmentID = d.DepartmentID;

--4. List of all employees, with department details if they belong to a department

SELECT e.EmployeeID, e.EmployeeName, d.DepartmentID, d.DepartmentName
FROM Employee e
LEFT JOIN Department d ON e.DepartmentID = d.DepartmentID;

--5. List of all departments, along with employee details if they have at least one employee

SELECT e.EmployeeID, e.EmployeeName, d.DepartmentID, d.DepartmentName
FROM Department d
INNER JOIN Employee e ON e.DepartmentID = d.DepartmentID;

