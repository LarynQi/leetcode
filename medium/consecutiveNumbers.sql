-- https://leetcode.com/problems/consecutive-numbers/submissions/1153280810?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below
WITH tmp AS (
    SELECT num, (LAG(num) OVER(ORDER BY id)) AS "prev", (LEAD(num) OVER(ORDER BY id)) AS "next" FROM Logs
)
SELECT DISTINCT num AS "ConsecutiveNums" FROM tmp WHERE prev = num AND next = num;
