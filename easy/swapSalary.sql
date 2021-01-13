# https://leetcode.com/problems/swap-salary/

# https://leetcode.com/submissions/detail/442260351/
# 01/12/2021 18:04  

# Write your MySQL query statement below
UPDATE salary 
SET sex = CASE 
    WHEN sex = "m" THEN "f"
    WHEN sex = "f" THEN "m" 
    END;