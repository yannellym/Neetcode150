# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.


   if len(nums) == 1:
            return nums[0]
        
        store = {}
        for digit in nums:
            if digit in store:
                store[digit] += 1
            else:
                store[digit] = 1
                
        for key, value in store.items():
            if value == 1:
                return key
  
  # alternative
    from collections import Counter
        c = Counter(nums)
        res = sorted(c,key = lambda x:c[x])[0]
        return res
  # Python's XOR   
  class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity: o(n)
        # Space Complexity: o(1)
        # """
        # Variable to store the solution
        single_number_solution = 0

        # Loop to traverse all the numbers
        for value in nums:
            # this will go through each value and if it hasnt seen the value before,
            # it will add it to the single_number_solution var
            # if it has seen it, it will subtract it from single_number_solution var
            # at the end, we will have the single value in the var
            single_number_solution ^= value

        # Return the single number solution
        return single_number_solution
