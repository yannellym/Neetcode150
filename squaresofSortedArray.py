# 977. Squares of a Sorted Array
# Easy
# 7.3K
# 181
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
# 1.3M
# Submissions
# 1.8M
# Acceptance Rate
# 71.9%

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # create a result array filled with 0s and the length of nums
        res = [0] * len(nums)
        # create out pointers
        i = 0
        j = len(nums)-1
        # for every digit in nums, loop starting at the last digit
        for digit in range(len(nums)-1,-1,-1):
            # if the absolute value of the left digit in nums is greater than the right digit in nums
            # have the current index value of res equal to the left value in nums but squared
            # increment i to move on to the next num
            if abs(nums[i]) > abs(nums[j]):
                res[digit] = nums[i] **2
                i+=1
            else:
            # if the absolute value of the right digit in nums is greater than the left digit in nums
            # have the current index value of res equal to the right value in nums but squared
            # decrement j to move on to the next num
                res[digit] = nums[j]**2
                j-=1 
        return res
      

# alternative solution
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        res = [0] * len(nums)
     

        for digit in nums:
            res[i] = digit**2
            i+=1
        return sorted(res)
