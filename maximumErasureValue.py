# 1695. Maximum Erasure Value
# Medium
# 2.6K
# 43
# company
# Amazon
# company
# Adobe
# Cashfree
# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 

# Example 1:

# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].
# Example 2:

# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
# Accepted
# 111.9K
# Submissions
# 194.4K
# Acceptance Rate
# 57.6%


class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        win_s = 0
        store = {}
        res = 0

        # for every num in nums 
        for win_e in range(len(nums)):
            # add it to the store
            store[nums[win_e]] = 1 + store.get(nums[win_e], 0)

            # while the value of the num in store is greater than 1 (repeats)
            while store[nums[win_e]] > 1: 
                # lets subtract 1 from that value so we have 1 less
                store[nums[win_s]] -= 1 
                # if the value ever becomes 0
                if store[nums[win_s]] == 0:
                    # lets delete it as we dont need that on our window
                    del store[nums[win_s]]
                # make the window smaller to fit our condition
                win_s += 1
            # set the res to equal the max between res and the sum of the store's keys)
            res = max(res, sum(store.keys()))
        return res


            



            


