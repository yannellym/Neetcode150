# 128. Longest Consecutive Sequence
# Medium

# 13159

# 543

# Add to List

# Share
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        store = set(nums)
        longest = 0
        
        for i in nums:
            length = 0
            if i-1 not in store:
                length = 1
                while (i + length) in store:
                    length += 1
                longest = max(length, longest)
        return longest
            
