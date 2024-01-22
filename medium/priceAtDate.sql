-- https://leetcode.com/problems/product-price-at-a-given-date/submissions/1153371388?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below
WITH inserted AS (
    SELECT * FROM Products UNION
    SELECT product_id, 10 AS "new_price", "" AS "change_date" FROM Products GROUP BY product_id
),
tmp AS (
    SELECT product_id, new_price, change_date FROM inserted WHERE change_date <= "2019-08-16"
),
maxs AS (
    SELECT product_id, MAX(change_date) AS "max" FROM tmp GROUP BY product_id
)
SELECT p.product_id, p.new_price as "price" FROM inserted AS p, maxs AS m WHERE p.change_date = m.max AND p.product_id = m.product_id;
