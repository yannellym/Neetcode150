# 1984. Minimum Difference Between Highest and Lowest of K Scores
# Easy

# 562

# 93

# Add to List

# Share
# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

# Return the minimum possible difference.

 

# Example 1:

# Input: nums = [90], k = 1
# Output: 0
# Explanation: There is one way to pick score(s) of one student:
# - [90]. The difference between the highest and lowest score is 90 - 90 = 0.
# The minimum possible difference is 0.
# Example 2:

# Input: nums = [9,4,1,7], k = 2
# Output: 2
# Explanation: There are six ways to pick score(s) of two students:
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
# - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
# The minimum possible difference is 2.


class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
      # sort the array first
        nums.sort()
        left = 0
        # the right is k - 1 because you want the window to be of size k
        # the arr is 0 index 
        right = k - 1
        # make this the largest val possible
        res = float('inf')
        
        # while right is less than the length of nums (our window is valid)
        while right < len(nums):
            # choose the min between res or the diff of the right and the left
            res = min(res, nums[right] - nums[left])
            # increase the left and right so the window keeps moving
            left += 1
            right += 1
        return res
        
