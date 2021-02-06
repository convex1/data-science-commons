
--- group_id | score |
    123      | 0.76
    123      | 0.85
    123      | 0.98

--to rank (with tie) records within a group in decreasing order of their score
select group_id, score, dense_rank() parition by (group_id order by score desc);

--to rank (with no tie) records within a group in decreasing order of their score
select group_id, score, row_number() parition by (group_id order by score desc);