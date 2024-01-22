-- https://leetcode.com/problems/count-salary-categories/submissions/1153292595?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below
-- SELECT low_count AS "Low Salary", avg_count AS "Average Salary", high_count AS "High Salary"  FROM (SELECT COUNT(*) AS "low_count" FROM Accounts WHERE income < 20000) AS low, (SELECT COUNT(*) AS "avg_count" FROM Accounts WHERE income >= 20000 AND income <= 50000) AS average, (SELECT COUNT(*) AS "high_count" FROM Accounts WHERE income > 50000) AS high;

SELECT "Low Salary" AS "category", low_count AS "accounts_count" FROM (SELECT COUNT(*) AS "low_count" FROM Accounts WHERE income < 20000) AS low UNION

SELECT "Average Salary", avg_count FROM (SELECT COUNT(*) AS "avg_count" FROM Accounts WHERE income >= 20000 AND income <= 50000) AS average UNION

SELECT "High Salary", high_count FROM (SELECT COUNT(*) AS "high_count" FROM Accounts WHERE income > 50000) AS high;

-- SELECT (SELECT COUNT(*) FROM Accounts WHERE income < 20000) AS "Low Salary",
-- SELECT (SELECT COUNT(*) FROM Accounts WHERE income >= 20000 AND income <= 50000) AS "Average Salary",
-- SELECT (SELECT COUNT(*) FROM Accounts WHERE income > 50000) AS "High Salary"
-- ;
