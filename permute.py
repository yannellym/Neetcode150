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

        # create an array for our results
        results = []

        # if the length of the nums is 1, return an array of a copy of that array
        if len(nums) == 1:
            return [nums[:]]
        
        # iterate the length on nums
        for i in range(len(nums)):
            # pop the first value
            n = nums.pop(0)
            # call permute on nums and save it on the perms var
            perms = self.permute(nums)
            # this will end up being 
            # [3]
            # [2]

            # at this point it will get called to return like our code above. We return a copy
            # we then go next to this code below

            # for every perm arr in perms
            # perms = [[3], [2]]
            for perm in perms:
                # append the value we popped
                # perms [[3,1], [2,1]]
                perm.append(n)
            
            # it iwll go again and append the next number we popped
            # perms = [[3,1,2], [2,1,3]]
            # add these arrs of perms to results
            results.extend(perms)
            # append the n again to the number so we can go again
            nums.append(n)
        return results



# https://www.youtube.com/watch?v=s7AvT7cGdSo
