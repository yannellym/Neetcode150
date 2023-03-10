# 2535. Difference Between Element Sum and Digit Sum of an Array
# Easy
# 332
# 10
# Companies
# You are given a positive integer array nums.

# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.

# Note that the absolute difference between two integers x and y is defined as |x - y|.

 

# Example 1:

# Input: nums = [1,15,6,3]
# Output: 9
# Explanation: 
# The element sum of nums is 1 + 15 + 6 + 3 = 25.
# The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
# The absolute difference between the element sum and digit sum is |25 - 16| = 9.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0
# Explanation:
# The element sum of nums is 1 + 2 + 3 + 4 = 10.
# The digit sum of nums is 1 + 2 + 3 + 4 = 10.
# The absolute difference between the element sum and digit sum is |10 - 10| = 0.
 

# Constraints:

# 1 <= nums.length <= 2000
# 1 <= nums[i] <= 2000
# Accepted
# 50.1K
# Submissions
# 58.5K
# Acceptance Rate
# 85.6%

class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # get the sum of nums
        esum = sum(nums)
        dsum = 0
        # join every number and convert to string, then split
        digits = [list(x) for x in (map(str, [num for num in nums]))]
       
        for sub in digits:
            for num in sub:
                dsum += eval(num)
    

        return abs(esum - dsum)


        # alternative 

        x=sum(nums)
        m=list(map(int,list(''.join(str(x) for x in nums))))
        z=sum(m)
        return abs(x-z)
