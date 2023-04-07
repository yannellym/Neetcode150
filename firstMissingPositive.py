# 41. First Missing Positive
# Hard
# 13.6K
# 1.6K
# Companies
# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# Accepted
# 861.6K
# Submissions
# 2.3M
# Acceptance Rate
# 36.7%



class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # append a zero to the end so we can compare all numbers
        nums.append(0)
        # get the length of nums
        n = len(nums)
        # lets make an array the length of n, filled with 0s. ex [0,0,0,0]
        store = [0 for i in range(n)]

        # iterate n times
        for i in range(n):
            # if the number at nums[i] is not a negative and it is less than or equal to n
            if nums[i] > 0 and nums[i] <= n:
                # change the value at the store to have a +1
                # we do -1 so we can have the correct/index place in the store
                store[nums[i]-1] += 1
            
        # store is [1,1,0,0] for nums[1,2,0]
        # iterate through the length of the store
        for i in range(len(store)):
            # if the ith element of the store (first element that equals 0)
            if store[i] == 0:
                # return i + 1 because itll be the first element that is missing in our nums arr
                # +1 so you can get the right index
                return i+1
