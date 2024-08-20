
Testcase
Testcase
Test Result
Test Result
Accepted
Code
610. Triangle Judgement
Solved
Easy
Topics
Companies
SQL Schema
Pandas Schema
Table: Triangle

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.
 

Report for every three line segments whether they can form a triangle.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
Output: 
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+
Seen this question in a real interview before?
1/5

# Write your MySQL query statement below
select x,y,z, (
    CASE
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END
) as triangle from Triangle

/* triangle inequality theorem. This theorem states that the sum of the lengths of any two sides must be greater than the length of the third side. 

*/
