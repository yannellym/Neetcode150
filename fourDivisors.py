# 1390. Four Divisors
# Medium
# 327
# 178
# company
# Capital One
# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

# Example 1:

# Input: nums = [21,4,7]
# Output: 32
# Explanation: 
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.
# Example 2:

# Input: nums = [21,21]
# Output: 64
# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 104
# 1 <= nums[i] <= 105
# Accepted
# 26.1K
# Submissions
# 63.4K
# Acceptance Rate
# 41.2%

class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
  
        res = 0

        for num in nums:
            count = 0
            div_sum = 0

            for divisor in range(1, int(num**0.5) + 1):
                if num % divisor == 0:
                    count += 1
                    div_sum += divisor

                    # Check if divisor is distinct from its corresponding quotient
                    if num // divisor != divisor:
                        count += 1
                        div_sum += num // divisor

                    if count > 4:
                        break

            if count == 4:
                res += div_sum

        return res

# Consider the number num = 12. The divisors of 12 are 1, 2, 3, 4, 6, and 12. When iterating through the divisors, we start with divisor = 1. At this point, the condition num // divisor != divisor is not satisfied because 1 is equal to num // divisor (which is also 1).

# Next, we move to divisor = 2. Again, the condition is not satisfied because 2 is equal to num // divisor, which is 6.

# But when we reach divisor = 3, the condition num // divisor != divisor is satisfied because 3 is not equal to num // divisor, which is 4. In this case, we increment the count variable and add num // divisor to the div_sum variable.

# The purpose of this condition is to ensure that we only count distinct pairs of divisors. If a divisor and its corresponding quotient are the same, it means we are counting the same divisor twice, which is incorrect.
