# 704. Binary Search
# Easy
# 7.7K
# 166
# Companies
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # declare both variables low and high
        # low will be at 0 to represent the beginning of our array
        # high will be at len(nums) - 1 to represent the end of the array
        low = 0
        high = len(nums) - 1
        # while low is less than or equal to high (to avoid out of bounds error)
        while low <= high:
            middle = (high + low) // 2
            # if the mid digit is less than the target element,
            # this means that the target element is on the right portion
            if nums[middle] < target:
                # low will now equal the middle index plus 1
                low = middle +1
            # if the mid digit is greater than the target element,
            # this means that the target element is on the left portion
            elif nums[middle] > target:
                # high will now equal the middle index minus 1
                high = middle - 1
            else:
                # if we made it here, it means we found the digit!
                # return it!
                return middle
        # return -1 if we do not find the digit in our array
        return -1
