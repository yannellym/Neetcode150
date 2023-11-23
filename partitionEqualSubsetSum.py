416. Partition Equal Subset Sum
Solved
Medium
Topics
Companies
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Check if the sum of numbers is odd
        if sum(nums) % 2:
            return False # Return 0 if the sum is odd (no equal partition is possible)

        # Initialize a set with a single element 0
        st = set([0])

        # Iterate through each number in the list
        for i in nums:
            # Iterate through each element in the current set
            for j in list(st):
                # Add the sum of the current number and the element in the set to the set
                st.add(i + j)

                # Check if the sum equals half of the total sum of numbers
                if i + j == sum(nums) // 2:
                    return True  # Return True if an equal subset sum is found
            print(st)
        return False  # Return False if no equal subset sum is found
