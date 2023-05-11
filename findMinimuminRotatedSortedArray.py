# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
  
#   153. Find Minimum in Rotated Sorted Array
# Medium
# 10.4K
# 476
# Companies
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.
# Accepted
# 1.3M
# Submissions
# 2.6M
# Acceptance Rate
# 48.9%

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # choose a random number from nums to be the min
        res = nums[0]

        l = 0
        r= len(nums)-1

        while l <= r:
            # if we're within the sorted array (left)
            if nums[l] < nums[r]:
                # choose the left most element since it will be the smallest
                res = min(res, nums[l])
                break
            # compute the middle 
            m = (l+r) //2
            # check if this is the min
            res = min(res, nums[m])
            # if the middle element is greater than the one at the left, 
            if nums[m] >= nums[l]:
                # move the left to be equal to m+1 as we want the other half of the array
                l = m+1
            else:
                r = m-1
        return res
