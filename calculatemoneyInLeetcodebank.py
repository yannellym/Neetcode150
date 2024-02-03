https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/?envType=daily-question&envId=2024-01-30

1716. Calculate Money in Leetcode Bank
Solved
Easy
Topics
Companies
Hint
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

 

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
 

Constraints:

1 <= n <= 1000




class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 1
        res = 0

        for day in range(1, n + 1):
            print(day)
            '''
            7 % 7 == 0
            7 % 8 == 1
             .. 2 .. 3
            '''
            # if its day 8, 16.. it must be doing again
            if day % 7 == 1:  # Check if it's the first day of a week (Monday)
                counter = (day // 7 ) + 1  # Reset the counter at the beginning of each week

            res += counter
            counter += 1

        return res
