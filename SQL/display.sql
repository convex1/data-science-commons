---input
---group_table
--- group_id | score |
--- 123      | 0.85
--- 123      | 0.85
--- 123      | 0.98



--OFFSET helps decide the starting point to display in a query
--to start from the second most highest score

select group_id, score from group_table order by score desc offset 2 limit 10;

---output
--- group_id | score
    123      | 0.85
    123      | 0.85