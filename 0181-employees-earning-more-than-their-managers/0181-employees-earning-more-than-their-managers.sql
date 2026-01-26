# Write your MySQL query statement below
SELECT e.name as Employee from Employee e left JOIN Employee m on e.managerId = m.id where e.salary > m.salary and e.managerId is not null;