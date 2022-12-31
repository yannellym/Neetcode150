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
        # variable to store the result
        res = []
        # sort the original array for the search to be more efficient
        nums.sort()

        # get the index and value of every digit in nums
        for index, value in enumerate(nums):
            # if the index is greater than 0 (its not the first value in the array)
            #  and the digit at this index equals 
            # the previous digit, just continue. We dont want a duplicate digit.
            if index > 0 and value == nums[index - 1]:
                continue
            # declare the left and right variables
            left = index + 1
            right = len(nums) - 1

            # to make sure we dont go out of bounds
            while left < right:
                # keeping our sum with our fixed number and two pointers
                threesum = value + nums[left] + nums[right]

                if threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
                else:
                    # if this hits, our sum equals 0. SO we add the array to our res
                    res.append([value,nums[left],nums[right]])
                    # update the left pointer and the right one updates automatically
                    left += 1
                    # if we have the same fixed value and our left pointer is less than our right pointer:
                    # increase the left. 
                    # we need this so our left pointer doesnt cross our right pointer.
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    
        return res
