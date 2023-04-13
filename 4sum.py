# 18. 4Sum
# Medium
# 9K
# 1.1K
# Companies
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 

# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Accepted
# 726.7K
# Submissions
# 2M
# Acceptance Rate
# 35.9


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        store = []
        
        n = len(nums)
        
        nums.sort()
        
        # iterate n-3 times because we are looking for 4 numbers
        for i in range(n-3):
            # if the index is greater than 0 and equal to the previous, continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # iterate through the list start at i +1 and going to n-2 as we need 3 numbers
            for j in range(i+1,n-2):
                # if the index is greater than i +1 and equal to the previous, continue
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                    # set k to equal j + 1 to look for the other two numbers 
                k = j+1
                l = n-1
                # while k and l are not equal
                while k < l:
                    # get the four tuple
                    sub = [nums[i], nums[j], nums[k], nums[l]]
                    if sum(sub) < target:
                        k += 1
                    elif sum(sub) > target:
                        l -= 1
                    else:
                        # if the sum of the four tuple is equal to 0 , append it to the store
                        store.append(sub)
                        # increase the left pointer
                        k += 1
                        # check if k is still < than l and if the number at k is equal to the previous 
                        while k < l and nums[k] == nums[k-1]:
                            # increase k, we dont want repeated nums
                            k += 1
                        # check if k is still < than l and if the number at l is equal to the previous 
                        while k < l and nums[l] == nums[l-1]:
                            # increase l, we dont want repeated nums
                            l -= 1
                    
        return store
