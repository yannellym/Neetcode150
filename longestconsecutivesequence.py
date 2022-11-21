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
        # put them all in a set so you do not have repeated numbers
        nums2 = set(nums)
        res = 0
        # look through each number in your set
        for i in nums2:
            # if number  - 1 is not in the set
            # this means it doesnt have a left neighbor and is the start of a sequence.
            if i - 1 not in nums2:
                # set the length to 0
                length = 0
                # while the number + length is in our set, increment the length
                while i + length in nums2:
                    length += 1
                # choose the highest, either res or length
                res = max(length, res)
        return res
