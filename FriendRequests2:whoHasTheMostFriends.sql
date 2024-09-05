602. Friend Requests II: Who Has the Most Friends
Solved
Medium
Topics
Companies
Hint
SQL Schema
Pandas Schema
Table: RequestAccepted

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
(requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.
 

Write a solution to find the people who have the most friends and the most friends number.

The test cases are generated so that only one person has the most friends.

The result format is in the following example.

 

Example 1:

Input: 
RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
+--------------+-------------+-------------+
Output: 
+----+-----+
| id | num |
+----+-----+
| 3  | 3   |
+----+-----+
Explanation: 
The person with id 3 is a friend of people 1, 2, and 4, so he has three friends in total, which is the most number than any others.
 

Follow up: In the real world, multiple people could have the same most number of friends. Could you find all these people in this case?

Seen this question in a real interview before?
1/5
Yes
No
Accepted
160K
Submissions
275.2K
Acceptance Rate
58.1%


# Write your MySQL query statement below

-- Create a common table expression (CTE) named CTE
WITH CTE AS (
    -- Select requester_id as id from RequestAccepted table
    SELECT requester_id AS id
    FROM RequestAccepted
    UNION ALL
    -- Select accepter_id as id from RequestAccepted table
    SELECT accepter_id AS id
    FROM RequestAccepted
)
-- Counts the number of times each id appears in the CTE.
-- It counts all rows that fall into each id group, which gives you the total number of interactions for each id.
SELECT id, COUNT(*) AS num
FROM CTE
-- Group by id to get the count of distinct accepter_id for each id
GROUP BY id
-- Order by the count in descending order
ORDER BY num DESC
-- Limit the result to the top 1 id with the highest count
LIMIT 1
