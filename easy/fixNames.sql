-- https://leetcode.com/problems/fix-names-in-a-table/submissions/1153175730?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below
SELECT user_id, CONCAT(UPPER(SUBSTR(name, 1, 1)), LOWER(SUBSTR(name, 2))) AS "name" FROM Users ORDER BY user_id;
