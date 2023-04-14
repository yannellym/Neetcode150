# 219. Contains Duplicate II
# Easy
# 4.7K
# 2.6K
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


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        

        # sliding window technique
        # create a set to store the values that fit into the window.
        window = set()
        L = 0
        # iterate through nums
        for R in range(len(nums)):
            # if our window is now too big
            if R - L > k:
                # remove the first value of the window
                window.remove(nums[L])
                L +=1
            # if the number is in the window
            if nums[R] in window:
                return True
            # add the new num
            window.add(nums[R])
        return False
