-- https://leetcode.com/problems/delete-duplicate-emails/submissions/1153187795?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below
DELETE p1 FROM Person p1, Person p2 WHERE p1.email = p2.email AND p1.id > p2.id;
