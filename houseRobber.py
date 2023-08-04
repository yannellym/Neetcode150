# 198. House Robber
# Medium
# 16.9K
# 328
# Companies
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
# Accepted
# 1.5M
# Submissions
# 3.1M
# Acceptance Rate
# 49.3%

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #. create two variables to hold our robbed amounts
        robbed1 = 0
        robbed2 = 0

        # For every amount in the houses:
        for amount in nums:
            # in a temp, save the max amount of either:
              # the new amount and robbed 1

            # [rob1, rob2, n , n +1, ...  ]
            # if we want to rob this amount, we can either rob the amount with rob 1 or 
            # just do rob2 (not with amount since it cant be next to each other)
            temp = max(amount + robbed1, robbed2)
            # now we update robbed 1 to to be robbed 2 since we're getting that last value used.
            robbed1 = robbed2
            # robbed 2 will now be our temp since we need the updated total so far.
            robbed2 = temp
        return temp


        #https://www.youtube.com/watch?v=73r3KWiEvyk
