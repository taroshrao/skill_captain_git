CREATE TABLE Employees (
  ID INT,
  Name VARCHAR(255),
  Department VARCHAR(255)
);


SELECT Department, COUNT(*) AS TotalEmployees
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 2
ORDER BY COUNT(*) DESC;
