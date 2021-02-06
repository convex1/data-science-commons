---input
---group_table
--- group_id | score |
--- 123      | 0.85
--- 123      | 0.85
--- 123      | 0.98




--to rank (with tie) records within a partition (group in this case) in decreasing order of their score

select group_id, sum(score) as sum_score, avg(score) avg_score, count(score) count_score from group_table;

---output
--- group_id | sum_score | avg_score | count_score
    123      | 2.68 | 0.893 | 3