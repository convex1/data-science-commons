---input
---group_table
--- group_id | score | city
    123      | 0.85  | NY
    123      | 0.85  | BLR
    123      | 0.98  | DEN



select * from group_table where group_id = 123 and score > 0.01;

--- group_id | score | city
    123      | 0.85  | NY
    123      | 0.85  | BLR
    123      | 0.98  | DEN


select * from group_table where group_id = 1678 or score > 0.01;

--- group_id | score | city
    123      | 0.85  | NY
    123      | 0.85  | BLR
    123      | 0.98  | DEN




select * from group_table where group_id != 123;

--different way of writing the above query

select * from group_table where not group_id = 123;

--- group_id | score | city
