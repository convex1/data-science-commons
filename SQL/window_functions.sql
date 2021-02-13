---input
---group_table
--- group_id | score |
--- 123      | 0.85
--- 123      | 0.85
--- 123      | 0.98




--to rank (with tie) records within a partition (group in this case) in decreasing order of their score

select group_id, score, dense_rank() over(partition by group_id order by score desc) rank from group_table;

---output
group_id | score | rank
123      | 0.98  | 1
123      | 0.85  | 2
123      | 0.76  | 2




--to rank (with no tie) records within a partition (group in this case) in decreasing order of their score

select group_id, score, row_number() over(partition by group_id order by score desc) rank;

---output
group_id | score | rank
123      | 0.98  | 1
123      | 0.85  | 2
123      | 0.76  | 3




--to get immediate previous value of row/records within a partition (group in this case)

select group_id, score, lag(score,1) over(partition by group_id) previous_score;

---output
group_id | score | rank
123      | 0.85  | null
123      | 0.85  | 0.85
123      | 0.98  | 0.85




--to get immediate next value of row/records within a partition (group in this case)

select group_id, score, lead(score,1) over(partition by group_id) next_score;

---output
group_id | score | rank
123      | 0.85  | 0.85
123      | 0.85  | 0.98
123      | 0.98  | null




--to calculate average within a partition (group in this case)

select group_id, score, avg(score) over(partition by group_id) partition_average;

---output
group_id | score | partition_average
123      | 0.85  | 0.893
123      | 0.85  | 0.893
123      | 0.98  | 0.893



--to calculate running sum within a partition (group in this case)

select group_id, score, sum(score) over(partition by group_id) partition_sum;

---output
group_id | score | partition_sum
123      | 0.85  | 2.68
123      | 0.85  | 2.68
123      | 0.98  | 2.68



--to calculate total sum of values (score) within a partition (group in this case)

select group_id, score, sum(score) over(partition by group_id) partition_sum;

---output
group_id | score | partition_sum
123      | 0.85  | 2.68
123      | 0.85  | 2.68
123      | 0.98  | 2.68



--to calculate first value of within a partition (group in this case)

select group_id, score, first_value(score) over(partition by group_id order by score asc) partition_first;

---output
group_id | score | partition_first
123      | 0.85  | 0.85
123      | 0.85  | 0.85
123      | 0.98  | 0.85



--to calculate last value of within a partition (group in this case)

select group_id, score, last_value(score) over(partition by group_id order by score desc) partition_last;

---output
group_id | score | partition_last
123      | 0.85  | 0.98
123      | 0.85  | 0.98
123      | 0.98  | 0.98



--to calculate last value of within a partition (group in this case)

select group_id, score, percent_rank over(partition by group_id order by score desc) percentage_rank;

---output
group_id | score | percentage_rank
123      | 0.85  | 0
123      | 0.85  | 0.5
123      | 0.98  | 1