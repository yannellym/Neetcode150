# 540. Single Element in a Sorted Array
# Medium
# 8.3K
# 127
# Companies
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105
# Accepted
# 422.9K
# Submissions
# 716.7K
# Acceptance Rate
# 59.0%

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # while left is less than right
        while left < right:
            # take the mid point
            mid = (left + right) // 2
            # if the index of the mid is odd
            if mid % 2 == 1:
                # take one away so it is even
                mid -= 1
            # if the digit at the mid point of nums is equal to the index at midpoint + 1
            if nums[mid] == nums[mid + 1]:
                # have the left equal mid + 2
                left = mid + 2
            else:
                right = mid
        
        return nums[left]


        #    def helper():
        #     xor = 0
        #     for i in nums:
        #         xor ^= i
        #     return xor
        # return helper()
