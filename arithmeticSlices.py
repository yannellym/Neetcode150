413. Arithmetic Slices
Solved
Medium
Topics
Companies
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
Accepted
284.6K
Submissions
437.6K
Acceptance Rate
65.0%


class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        count = 0  # Count of arithmetic subarrays ending at the current index
        total = 0  # Total count of all arithmetic subarrays encountered

        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                count += 1
                total += count
            else:
                count = 0  # Reset the count when a non-arithmetic subarray is encountered

        return total


# alternative

def numberOfArithmeticSlices(nums):
    # Check if the length of the array is less than 3, in which case there are no arithmetic subarrays.
    if len(nums) < 3:
        return 0

    # Initialize a dynamic programming (DP) array to store the count of arithmetic subarrays ending at each index.
    dp = [0] * len(nums)
    
    # Initialize a variable to keep track of the total count of arithmetic subarrays.
    count = 0

    # Iterate through the array starting from the third element (index 2).
    for i in range(2, len(nums)):
        # Check if the current element and the previous two elements form an arithmetic subarray.
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            # If yes, update the count of arithmetic subarrays ending at index i.
            dp[i] = dp[i-1] + 1
            
            # Add the count of arithmetic subarrays ending at index i to the total count.
            count += dp[i]

    # Return the total count of arithmetic subarrays.
    return count

# Example 1
nums1 = [1, 2, 3, 4]
print(numberOfArithmeticSlices(nums1))  # Output: 3

# Example 2
nums2 = [1]
print(numberOfArithmeticSlices(nums2))  # Output: 0
