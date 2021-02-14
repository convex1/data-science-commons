---input
---group_table
group_id | score | char_value
123      | 0.85  |  A
123      | 0.85  |  B
123      | 0.98  |  C




--to rank (with tie) records within a partition (group in this case) in decreasing order of their score

select group_id, sum(score) as sum_score, avg(score) avg_score, count(score) count_score from group_table
group by group_id;

---output
group_id | sum_score | avg_score | count_score
123      | 2.68 | 0.893 | 3




select group_id, string_agg(char_value, ',') as char_values from group_table
group by group_id;

---output
group_id | char_values
123      | A,B,C