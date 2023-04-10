# 1498. Number of Subsequences That Satisfy the Given Sum Condition
# Medium
# 1.9K
# 165
# Companies
# You are given an array of integers nums and an integer target.

# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [3,5,6,7], target = 9
# Output: 4
# Explanation: There are 4 subsequences that satisfy the condition.
# [3] -> Min value + max value <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)
# Example 2:

# Input: nums = [3,3,6,8], target = 10
# Output: 6
# Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
# [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
# Example 3:

# Input: nums = [2,3,3,4,6,7], target = 12
# Output: 61
# Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
# Number of valid subsequences (63 - 2 = 61).
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
# 1 <= target <= 106
# Accepted
# 41.5K
# Submissions
# 110.5K
# Acceptance Rate
# 37.5%

class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # set the modulo value to 10^9 + 7
        MOD = 10**9 + 7
        # sort the array in non-decreasing order
        nums.sort()
        # get the length of the array
        n = len(nums)
        # initialize left and right pointers
        left, right = 0, n - 1
        # initialize count variable to store number of subsequences
        count = 0
        # loop until left pointer reaches or passes right pointer
        while left <= right:
            # check if sum of left and right elements is greater than target
            if nums[left] + nums[right] > target:
                # if yes, decrement the right pointer
                right -= 1
            else:
                # if not, add the number of subsequences that can be formed
                # by taking the current left element and any of the elements
                # in the range [left, right] to the count variable
                # the number of subsequences that can be formed is equal to 2^(right - left)
                # https://www.programiz.com/python-programming/methods/built-in/pow
                count += pow(2, right - left, MOD)
                # increment the left pointer
                left += 1
        # return the count modulo MOD
        return count % MOD
