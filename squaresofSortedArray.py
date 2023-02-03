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
        # Create a resultant list
        result_list = [0]*len(nums)

        left = 0
        right = len(nums) - 1

        # iterate the resultant list from the end, 
        # this is because we want to the final result to be in a rising order
        for result_pointer in range(len(nums)-1, -1 , -1):
            if abs(nums[left])>abs(nums[right]):
                result_list[result_pointer] = nums[left]*nums[left]
                left += 1
            else:
                result_list[result_pointer] = nums[right]*nums[right]
                right -=1
        
        return result_list

      

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
