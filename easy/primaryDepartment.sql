-- https://leetcode.com/problems/primary-department-for-each-employee/submissions/1153238357?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below
SELECT e1.employee_id, e1.department_id FROM Employee AS e1 WHERE e1.primary_flag = "Y" OR (SELECT COUNT(*) FROM Employee AS e2 WHERE e1.employee_id = e2.employee_id) = 1;
