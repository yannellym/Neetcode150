
613. Shortest Distance in a Line
Solved
Easy
Topics
SQL Schema
Pandas Schema
Table: Point

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
+-------------+------+
In SQL, x is the primary key column for this table.
Each row of this table indicates the position of a point on the X-axis.
 

Find the shortest distance between any two points from the Point table.

The result format is in the following example.

 

Example 1:

Input: 
Point table:
+----+
| x  |
+----+
| -1 |
| 0  |
| 2  |
+----+
Output: 
+----------+
| shortest |
+----------+
| 1        |
+----------+
Explanation: The shortest distance is between points -1 and 0 which is |(-1) - 0| = 1.
 

Follow up: How could you optimize your solution if the Point table is ordered in ascending order?

# Write your MySQL query statement below
SELECT 
    MIN(ABS(p1.x - p2.x)) AS shortest
FROM 
    point p1
INNER JOIN 
    point p2 ON p1.x != p2.x;
-- '''
-- For the point table with values 1, 2, 3, the query will generate all pairs where the x values are not equal. The Cartesian product would be filtered by the condition p1.x != p2.x.

-- When p1.x = 1, p2.x can be 2 or 3.
-- When p1.x = 2, p2.x can be 1 or 3.
-- When p1.x = 3, p2.x can be 1 or 2.
-- '''

-- The MIN() function selects the smallest value from the results produced by ABS(p1.x - p2.x) for all pairs of rows where p1.x and p2.x are distinct.
