# 560. Subarray Sum Equals K
# Medium
# 17.1K
# 502
# Companies
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107
# Accepted
# 929.4K
# Submissions
# 2.1M
# Acceptance Rate
# 43.8%

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # start off with a dict of sum of 0 with a value of 1
        # this represents the left most value not represented in nums
        sumDict = {0:1}
        count = 0
        summ = 0

        # for each number in nums
        for num in nums:
            # add the  num to the sum
            # we're keeping track of a continuous sum
            summ += num
            # if the sum - k is in the dictionary,
            # that means we have a subarray of sum k, 
            # add the value of sum-k to the count
            if summ-k in sumDict:
                count += sumDict[summ-k]
            # if the sum is in the sumdictionary, it means that we have it already
            # just add 1 to the dictionary
            if summ in sumDict:
                sumDict[summ] += 1
            else:
                # if its not there, have it equal 1
                sumDict[summ] = 1
        return count

        #https://www.youtube.com/watch?v=bqN9yB0vF08
