# https://leetcode.com/problems/duplicate-emails/

# https://leetcode.com/submissions/detail/439964527/
# 01/07/2021 13:13  

# Write your MySQL query statement below
SELECT Email FROM Person GROUP BY Email HAVING COUNT(*) > 1;