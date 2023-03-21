# 2348. Number of Zero-Filled Subarrays
# Medium
# 1.5K
# 48
# Companies
# Given an integer array nums, return the number of subarrays filled with 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation: 
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
# Example 2:

# Input: nums = [0,0,0,2,0,0]
# Output: 9
# Explanation:
# There are 5 occurrences of [0] as a subarray.
# There are 3 occurrences of [0,0] as a subarray.
# There is 1 occurrence of [0,0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
# Example 3:

# Input: nums = [2,10,2019]
# Output: 0
# Explanation: There is no subarray filled with 0. Therefore, we return 0.
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# Accepted
# 79.2K
# Submissions
# 120.5K
# Acceptance Rate
# 65.7%

class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # get the length of nums
        n = len(nums)
        # res will keep our total sum of all subarrays filled with zeroes
        res = 0
        # will serve as our temporary count
        count = 0
        # iterate through n
        for i in range(n):
            # if the digit at the current index of nums is equal to 0
            if nums[i] == 0:
                # add one to the count
                count += 1
                # add the count to our res
                res += count
            else:
                # if its not, then the count is 0
                count = 0
        return res

        # how it works
        '''
        Ex. [0,0,0,2,0,0]
        - index = 0, count = 0, res = 0:    nums[i] = 0   count +=1, res += count
        - index = 1, count = 1, res = 1:    nums[i] = 0   count +=1, res += count
        - index = 2, count = 2, res = 3:    nums[i] = 0   count +=1, res += count
        - index = 3, count = 3, res = 6:    nums[i] = 2   count  = 0
        - index = 4, count = 1, res = 7:    nums[i] = 0   count +=1, res += count
        - index = 5, count = 2, res = 9:    nums[i] = 0   count +=1, res += count
        
        '''
