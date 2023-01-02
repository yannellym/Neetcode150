# 2367. Number of Arithmetic Triplets
# Easy
# 608
# 23
# Companies
# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.

 

# Example 1:

# Input: nums = [0,1,4,6,7,10], diff = 3
# Output: 2
# Explanation:
# (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
# (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
# Example 2:

# Input: nums = [4,5,6,7,8,9], diff = 2
# Output: 2
# Explanation:
# (0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
# (1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.


class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        s = set(nums)
        count = 0
        # for each number in nums
        for num in nums:
            # if num plus diff is in S and num + diff + diff is in s:
            # increment the count
            # this works because    see below:
            if (num + diff) in s and (num + diff + diff) in s:
                count += 1
        return count


        
        # if you take the current number and add it to the target
        # 1 + 3 = 4. yes
        # if you take the current number and add the target twice
        # 1 + 3 + 3 = 7 yes
        # if both answers are in the array, increment count
