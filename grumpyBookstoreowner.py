1052. Grumpy Bookstore Owner
Solved
Medium
Topics
Companies
Hint
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
Example 2:

Input: customers = [1], grumpy = [0], minutes = 1
Output: 1
 

Constraints:

n == customers.length == grumpy.length
1 <= minutes <= n <= 2 * 104
0 <= customers[i] <= 1000
grumpy[i] is either 0 or 1.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
172.2K
Submissions
269.4K
Acceptance Rate
63.9%
Topics
Array
Sliding Window



  class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        window_total = 0
        window_maxi = 0

        satisfied = 0

        win_s = 0

        for win_e in range(len(customers)):
            # if the owner wasn't grumpy, add it to the satisfied total
            if grumpy[win_e] == 0:
                satisfied += customers[win_e]
            # if the owner was grumpy, add it to the window total
            elif grumpy[win_e] == 1:
                window_total += customers[win_e]

            # if our window is greater than our minutes
            if win_e - win_s + 1 > minutes:
                # if the customer was there when the store owner was inititally grumpy, (win_S)
                # # remove that from total
                if grumpy[win_s] == 1:
                    window_total -= customers[win_s]
                # our window needs to shrink
                win_s += 1
            # take the max of window_maxi and window_total
            window_maxi = max(window_maxi, window_total)
        # the result will be the num of satisfied customers plus the highest window_maxi
        return satisfied + window_maxi





