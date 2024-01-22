-- https://leetcode.com/problems/last-person-to-fit-in-the-bus/submissions/1153401747?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below
-- WITH unity AS (
--     SELECT person_id, person_name, weight
-- )
-- WITH tmp AS (
--     SELECT person_name, SUM(weight) FROM Queue GROUP BY person_id HAVING MAX(tur)
-- )

-- WITH tmp AS (
--     SELECT q1.person_id, q1.person_name AS "last", q1.weight AS "last_weight", q1.turn, q2.weight FROM Queue AS q1, Queue AS q2 WHERE q1.person_id != q2.person_id AND q2.turn < q1.turn UNION SELECT person_id, person_name, weight, turn, 0 FROM Queue WHERE turn=1
-- ),
-- total_weights AS (SELECT last, SUM(weight) + last_weight AS "total_weight", turn FROM tmp GROUP BY last),
-- final AS (SELECT MAX(turn) AS "maximum" FROM total_weights WHERE total_weight <= 1000)
-- SELECT t.person_name AS "person_name" FROM Queue AS t, final AS f WHERE t.turn = f.maximum;

WITH tmp AS (
    SELECT q1.person_id, SUM(q2.weight) + q1.weight AS "total_weight", q1.turn FROM Queue AS q1, Queue AS q2 WHERE q1.person_id != q2.person_id AND q2.turn < q1.turn GROUP BY q1.person_id
),
final AS (SELECT IFNULL(MAX(turn), 1) AS "maximum" FROM tmp WHERE total_weight <= 1000)
SELECT t.person_name AS "person_name" FROM Queue AS t, final AS f WHERE t.turn = f.maximum;
