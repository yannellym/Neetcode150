Table: Cinema

+-------------+------+
| Column Name | Type |
+-------------+------+
| seat_id     | int  |
| free        | bool |
+-------------+------+
seat_id is an auto-increment column for this table.
Each row of this table indicates whether the ith seat is free or not. 1 means free while 0 means occupied.
 

Find all the consecutive available seats in the cinema.

Return the result table ordered by seat_id in ascending order.

The test cases are generated so that more than two seats are consecutively available.

The result format is in the following example.

 

Example 1:

Input: 
Cinema table:
+---------+------+
| seat_id | free |
+---------+------+
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |
+---------+------+
Output: 
+---------+
| seat_id |
+---------+
| 3       |
| 4       |
| 5       |
+---------+


# Write your MySQL query statement below
SELECT DISTINCT a.seat_id
FROM cinema a 
JOIN cinema b
#The reason we use = 1 in the condition ABS(a.seat_id - b.seat_id) = 1 is that we specifically want to compare adjacent seats — seats that are immediately next to each other.
  ON ABS(a.seat_id - b.seat_id) = 1
  AND a.free = 1 
  AND b.free = 1
ORDER BY a.seat_id;


-- Execution Walkthrough:
-- Step 1: Compare seat_id = 1 with seat_id = 2: Since seat_id = 2 is occupied (free = 0), seat_id = 1 is not included.
-- Step 2: Compare seat_id = 3 with seat_id = 4: Both are free (free = 1), so seat_id = 3 and seat_id = 4 are included in the result.
-- Step 3: Compare seat_id = 4 with seat_id = 5: Both are free (free = 1), so seat_id = 4 and seat_id = 5 are included in the result.
-- Step 4: Since we are using DISTINCT, seat_id = 4 is only included once.
