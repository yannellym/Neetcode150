# # 
# 78. Subsets
# Medium
# 13.8K
# 198
# Companies
# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# Accepted
# 1.4M
# Submissions
# 1.9M
# Acceptance Rate
# 74.8%

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # start with an array with an empty list
        res = [ [] ]

        # for every number is nums
        for i in nums:
            # iterate jth amount of times with j being the length of res
            for j in range(len(res)):
           
                #to the res append: combined res[j] and res[i]
                res.append(res[j]+[i])
        return res

        # basically, it will go through nums, and iterate the length of res,
        # it will add each subarray in res and append the [i] to it



#     Input
# nums =
# [1,2,3]

# Stdout
# [[]]
# [1]
# [[], [1]]
# [2]
# [[], [1], [2]]
# [1, 2]
# [[], [1], [2], [1, 2]]
# [3]
# [[], [1], [2], [1, 2], [3]]
# [1, 3]
# [[], [1], [2], [1, 2], [3], [1, 3]]
# [2, 3]
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3]]
# [1, 2, 3]


# [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
