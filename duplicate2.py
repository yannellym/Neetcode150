# 219. Contains Duplicate II
# Easy
# 4.5K
# 2.5K
# Companies
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105
# Accepted
# 643.1K
# Submissions
# 1.5M
# Acceptance Rate
# 42.5%

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # dic to store our indices
        dic = {}
        # for i in range of the length of nums
        for i in range(len(nums)):
            # if the digit of nums at index i is in dic, and index - the number stored at dic is <= to k
            # return True
            if nums[i] in dic and i - dic[nums[i]] <= k:
                return True
             # else, if its not in the dic, add it to the dic and store its index
            dic[nums[i]] = i
        # if the first condition above doesnt execute, return False
        return False
