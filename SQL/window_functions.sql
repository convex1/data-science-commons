---input
---group_table
--- group_id | score |
--- 123      | 0.85
--- 123      | 0.85
--- 123      | 0.98

--to rank (with tie) records within a partition (group in this case) in decreasing order of their score

select group_id, score, dense_rank() over(partition by group_id order by score desc) as rank from group_table;

---output
--- group_id | score | rank
    123      | 0.98  | 1
    123      | 0.85  | 2
    123      | 0.76  | 2

--to rank (with no tie) records within a partition (group in this case) in decreasing order of their score

select group_id, score, row_number() over(partition by group_id order by score desc);

---output
--- group_id | score | rank
    123      | 0.98  | 1
    123      | 0.85  | 2
    123      | 0.76  | 3


--to get immediate previous value of row/records within a partition (group in this case)

select group_id, score, lag(score,1) over(partition by group_id);

---output
--- group_id | score | rank
    123      | 0.85  | null
    123      | 0.85  | 0.85
    123      | 0.98  | 0.85

