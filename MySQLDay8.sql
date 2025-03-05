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
