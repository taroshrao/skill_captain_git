create database SkillCaptain;
use SkillCaptain;
CREATE TABLE Employees (
    ID INT PRIMARY KEY,  
    name VARCHAR(50),
    email VARCHAR(255),
    department VARCHAR(100),
    dateofbirth DATE,
    salary DECIMAL(15,2),
    IsActive TINYINT DEFAULT 1 
);

insert into Employees
VALUES
(1, 'Tarosh Rao', 'taroshrao@gmail.com', 'Data Science', '1990-08-08', 1200000.00, 1),
(2, 'Richa Bhardwaj', 'richa@gmail.com', 'HR', '1991-03-15', 2000000.50, 0);

SELECT * FROM Employees;

SELECT ID, name FROM Employees WHERE salary > 10000;
