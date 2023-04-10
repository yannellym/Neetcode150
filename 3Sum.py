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
        # sort the input array in order to place duplicates next to each other
        nums.sort()
        res = []
        # iterate through nums and get the index and the value
        for i, n in enumerate(nums):
            # if i is not the first one in the array, and the current value is equal to the previous value
            if i > 0 and nums[i] == nums[i-1]:
                # just continue, we dont want duplicates
                continue
            # we have a value so far. Ex, -1
            # lets initialize l as i +1 in order to search on the right
            l = i+1
            # r is initialized as len(nums)-1 to start at the end of the array and keep decreasing as necessary
            r = len(nums)-1
            # wile l and r are not equal
            while l < r :
                # lets save the three values in an array
                tnums = [n, nums[l], nums[r]]
                # get the sum of the three values
                tsum = sum(tnums)
                # if the sum is greater, decrease the right to make the sum smaller since the arr is sorted
                if tsum > 0:
                    r -= 1
                # if the sum is less than 0, increase the left to make the sum greater since the arr is sorted
                elif tsum < 0 :
                    l += 1
                # if its not greater nor less, add it to the res arr
                else:
                    res.append(tnums)
                    # increase the l pointer
                    l +=1
                    # there might be some edge cases where the number at index l is still the same, so we need
                    # to take care of this with a while loop. While nums l equals the previous value, and l < r
                    # we dont want the left pointer to pass the right pointer.
                    while nums[l] == nums[l-1] and l <r:
                        # increase the l
                        l +=1
        return res
                    
