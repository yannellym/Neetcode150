# 977. Squares of a Sorted Array
# Easy
# 7.8K
# 192
# Companies
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
 

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
# Accepted
# 1.4M
# Submissions
# 2M
# Acceptance Rate
# 71.9%


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []

        l = 0
        r = len(nums)-1
        # compute each square of left and right and see which one is bigger, append that
        # if one is bigger, increase or decrease the pointer.
        while l <= r:
            left = nums[l] ** 2
            right = nums[r] ** 2

            if left > right:
                res.insert(0, left)
                l +=1
            else:
                res.insert(0, right)
                r -=1
        return res
