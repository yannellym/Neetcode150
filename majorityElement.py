#    169. Majority Element
# Easy
# 13.6K
# 428
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?
# Accepted
# 1.6M
# Submissions
# 2.5M
# Acceptance Rate
# 63.9%

# Vayer Moore's algorithm
    
        count = 0
        candidate = None
        # go through each num in nums
        for num in nums:
            # if the count is 0, set the candidate to equal the current num
            # this will ensure that the candidate resets if it is not the major element
            if count == 0:
                candidate = num
            # if the count is NOT 0, update the count to be equal to:
            # count + 1 if the num equals the candidate, else count - 1
            count += (1 if num == candidate else -1)

        return candidate
