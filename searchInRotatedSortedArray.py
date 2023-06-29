# 33. Search in Rotated Sorted Array
# Medium
# 21.9K
# 1.3K
# company
# Apple
# company
# Yahoo
# company
# Amazon
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104
# Accepted
# 2.1M
# Submissions
# 5.3M
# Acceptance Rate
# 39.2%


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        


 


        l = 0
        r = len(nums) - 1

        while l <= r:
            middle = (l + r) // 2

            if nums[middle] == target:
                return middle

            # Check if the left portion is sorted
            if nums[l] <= nums[middle]:
                if target >= nums[l] and target < nums[middle]:
                    r = middle - 1
                else:
                    l = middle + 1
            # Right portion is sorted
            else:
                if target > nums[middle] and target <= nums[r]:
                    l = middle + 1
                else:
                    r = middle - 1

        return -1



'''
In the code provided, the condition if target >= nums[l] and target < nums[middle] is used to determine if the target element 
falls within the range of the left sorted portion of the array.

Let's revisit the example:

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
Initially, l = 0 and r = len(nums) - 1 = 6. The middle element is middle = (0 + 6) // 2 = 3, which corresponds to the value 7 
in nums. Since target is not equal to 7, we proceed to the next steps.

The code checks if the left portion [4, 5, 6, 7] is sorted. In this case, the left portion is sorted.

Next, the code enters the condition if target >= nums[l] and target < nums[middle], which translates to if 0 >= 4 and 0 < 7. 
Since this condition is false (0 is not greater than or equal to 4), it means that target does not fall within the range of 
the left sorted portion. Therefore, the search range is adjusted to the right side of the array, and l becomes middle + 1.

Continuing with the example, the code will search within the right portion [0, 1, 2] and eventually find the target element 0
at index 4.

'''
