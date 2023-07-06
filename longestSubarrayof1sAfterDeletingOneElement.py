# 1493. Longest Subarray of 1's After Deleting One Element
# Medium
# 3.1K
# 52
# company
# Yandex
# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# Accepted
# 142.7K
# Submissions
# 215.8K
# Acceptance Rate
# 66.1%

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialize all counters to 0
        prev = 0
        curr = 0
        ans = 0

        # look through each num in nums 
        for num in nums:
            # if the num is NOT 0
             # add it to the curr
            if num: 
                curr += 1
            else:
                # if the num is 0, we need to set our ans to the max between ans and curr+prev
                # this means that we have seen a full subarray of 1s and are now encountering a 0
                ans = max(ans, curr + prev)
                # now the prev quantity of 1's we have seen will be in prev
                prev = curr
                # our current will become 0 as we have a new count 
                curr = 0
        # we need to compute at the end of the loop as well in case we have a corner case. Ex [....111]
        ans = max(ans, curr + prev)
        # if the ans if the len of nums, we had no 0s so we need to return the ans - 1 else just return the answer
        return ans - 1 if (ans == len(nums)) else ans

        # https://www.youtube.com/watch?v=jhBrybXSFTs

