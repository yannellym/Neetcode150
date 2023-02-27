# 228. Summary Ranges
# Easy
# 2.5K
# 1.3K
# Companies
# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
 

# Constraints:

# 0 <= nums.length <= 20
# -231 <= nums[i] <= 231 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.
# Accepted
# 336.8K
# Submissions
# 714.7K
Acceptance Rate
47.1%


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # if we have an empty nums, return an empty array
        if not nums: return []
        # set our start and curr vars to be equal to the first elem in nums
        start = nums[0]
        curr = nums[0]
        end = None
        res = []
        # for every number after the first element:
        for n in nums[1:]:
            # add one to the current so we can compare 
            curr += 1
            # if the end equals the current (meaning we're still within a range)
            if n == curr:
                # update the end to be n (this digit)
                end = n
            else:
                # this means we do not have a range
                # if there's no end
                if not end:
                    # append the start string to the res
                    res.append(str(start))
                else:
                    # append the start string plus arrow plus string end
                    res.append(str(start)+"->"+str(end))
                # reset the vars
                start = n
                curr = n
                end = None
        # takes care of the last number in case it doesnt have a partner
        if not end:
            res.append(str(start))
        else:
            res.append(str(start)+"->"+str(end))
        return res
