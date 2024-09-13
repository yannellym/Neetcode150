Table: Seat

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
The ID sequence always starts from 1 and increments continuously.
 

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

The result format is in the following example.

 

Example 1:

Input: 
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
Output: 
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+
Explanation: 
Note that if the number of students is odd, there is no need to change the last one's seat.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
247.3K
Submissions
349.9K
Acceptance Rate
70.7%

  
  # Write your MySQL query statement below
SELECT
    (CASE
        # if id is even, decrease by 1
        WHEN id % 2 = 0 THEN id-1
        # if id is odd and the last one, just put the same id
        WHEN id % 2 != 0 AND id = (
            SELECT MAX(id)
            FROM Seat 
        ) THEN id
        # else, it is odd, so increase by 1
        ELSE id +1
    END) as id,   # the id column
    student      # the student column
FROM Seat  
ORDER BY id;