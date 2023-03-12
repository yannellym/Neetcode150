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
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         # start a list with an empty sublist
#         subsets = [[]]
#         # for every number in num 
#         for num in nums:
#             # loop ith amount of times with i being the len of the subsets
#             for i in range(len(subsets)):
#                 # choose the ith subset in the subsets arr
#                 currSubset = subsets[i]
#                 print(currSubset + [num])
#                 # to subsets, append the currsubset and the num
#                 subsets.append(currSubset + [num])
#         return subsets

#         # appended to subset each time
#         # [1]
#         # [2]
#         # [1, 2]
#         # [3]
#         # [1, 3]
#         # [2, 3]
#         # [1, 2, 3]
