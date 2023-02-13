# 46. Permutations
# Medium
# 14.7K
# 251
# Companies
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# Accepted
# 1.5M
# Submissions
# 2M
# Acceptance Rate
# 75.4%

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # as we can see on our last case,
        # if the length is one, return the original array
        if len(nums) == 1:
            return [nums[:]]

        # go through each index in nums
        for i in range(len(nums)):
            # pop the first element
            n = nums.pop(0)
            # recursively call permute func on nums that has been modified
            # ex, ex1 original = [1,2,3] -> [2,3] -> [3]
            perms = self.permute(nums)

            for perm in perms:
                # append the number that was popped from beginning
                perm.append(n)
            # add this new permutation to the result
            result.extend(perms)
            # append the n to the nums again
            nums.append(n)
        return result
#example1
#         [//1,2,3]        pop 1
#     [2,3]. [1,3] [1,2].  pop 2
# [3] [2]  [3] [1]. [2] [1]. we cant go any further so 
# add 3 to our perm, add 2 since we popped it, add 1 since we popped it.


# https://www.youtube.com/watch?v=s7AvT7cGdSo
