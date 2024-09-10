Delete Duplicate Emails
Solved
Easy
Topics
Companies
SQL Schema
Pandas Schema
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.

For Pandas users, please note that you are supposed to modify Person in place.

After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.

The result format is in the following example.

 

Example 1:

Input: 
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Output: 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
583.8K
Submissions
929.5K
Acceptance Rate
62.8%

# Write your MySQL query statement below

DELETE t2 
FROM Person t1
INNER JOIN Person t2 
WHERE 
    t2.id > t1.id AND 
    t2.email = t1.email;



-- INNER JOIN:
-- The query joins the Person table with itself. This is known as a self-join.
-- Conditions in the WHERE Clause:
-- t1.id > t2.id: This ensures that for each pair of records with the same email, the one with the larger id is considered for deletion.
-- t1.email = t2.email: This ensures that only records with the same email are compared.
-- DELETE Statement:
-- The DELETE t1 part specifies that the records from the Person table aliased as t1 should be deleted.
