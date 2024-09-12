Table: Users

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains information of the users signed up in a website. Some e-mails are invalid.
 

Write a solution to find the users who have valid emails.

A valid e-mail has a prefix name and a domain where:

The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
The domain is '@leetcode.com'.
Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Users table:
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 2       | Jonathan  | jonathanisgreat         |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
| 5       | Marwan    | quarz#2020@leetcode.com |
| 6       | David     | david69@gmail.com       |
| 7       | Shapiro   | .shapo@leetcode.com     |
+---------+-----------+-------------------------+
Output: 
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
+---------+-----------+-------------------------+
Explanation: 
The mail of user 2 does not have a domain.
The mail of user 5 has the # sign which is not allowed.
The mail of user 6 does not have the leetcode domain.
The mail of user 7 starts with a period.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
137.5K
Submissions
312K
Acceptance Rate
44.1%


# Write your MySQL query statement below
SELECT user_id, name, mail
FROM Users
-- Note that we also escaped the `@` character, as it has a special meaning in some regex flavors
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*\\@leetcode\\.com$';

-- ^: Ensures the pattern matches from the beginning of the string.
-- [a-zA-Z]: Matches the first character of the prefix, which must be a letter.
-- [a-zA-Z0-9_.-]*: Matches zero or more of the allowed characters (letters, digits, underscores, periods, and hyphens) that follow the initial letter. This part of the pattern defines the prefix.
-- \\@leetcode\\.com: Matches the literal string @leetcode.com.
-- $: Ensures the pattern matches until the end of the string.
