# 1838. Frequency of the Most Frequent Element
# Medium
# 2.3K
# 57
# Companies
# The frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.

 

# Example 1:

# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.
# Example 2:

# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
# Example 3:

# Input: nums = [3,9,6], k = 2
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 105
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # first we sort the array so all elements can be sorted by frequency
        nums.sort() 

        win_start = 0
        res = 0
        total = 0

        # iterate through nums
        for win_end in range(len(nums)):
            # add the right most element to total
            total += nums[win_end]

            # check if our window becomes invalid(meaning we have elements to replace than we have replacements=k)
            '''
            l      r
            [1,1,1,2,2,4]
            2(right most element) * 4(window length) > 5 (total)+ 2(amount we can replace)
            we're trying to make 2 the most frequent. So we multiply 2 nums[win_end] * len of the window. This tells us the sum of that
            window if it were multiplied by that number. Then, we have to check if it is greater than the total + k.
             (total + k is the amount that we can replace in total). If our left amount is greater than this, we have a window thats too big. 
             once this stops, we'll have our answer
            '''
            while nums[win_end] * (win_end - win_start+1) > total + k:
                total -= nums[win_start]
                # increment the left pointer to maintain our window
                win_start +=1
            # choose the max value between res and the size of the window
            res = max(res, (win_end - win_start+1))
        return res
# 1 <= nums[i] <= 105
# 1 <= k <= 105
# Accepted
# 41.5K
# Submissions
# 105.5K
# Acceptance Rate
# 39.4%
