# 15. 3Sum
# Medium

# 21473

# 1988

# Add to List

# Share
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [] # we will be returning an array of arrays
        nums.sort() # sort the array for efficiency
        
        for index, value in enumerate(nums):
        # if the index is greater than 0, and the value is the same as the previous one, continue
            if index > 0 and  value == nums[index - 1]: 
                continue
        
            left = index + 1
            right = len(nums) - 1
            while  left < right:
                threesum = value + nums[left] + nums[right]
                if threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
                else:
                    # append this to the response array
                    res.append([value, nums[left], nums[right]])
                    left += 1
                    # make sure it's not the same as previous, and that left is less than right
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return res
                
