# 435. Non-overlapping Intervals
# Medium
# 5.5K
# 152
# Companies
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

# Constraints:

# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104
# Accepted
# 340.4K
# Submissions
# 679.3K
# Acceptance Rate
# 50.1%

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sort the interval array so we get sorted subarrays
        intervals.sort()
        # save the end value of the first subarray
        prevEnd = intervals[0][1]
        # res will keep our count
        res = 0

        # for every start and end value in a subarray starting at index 1
        for start, end in intervals[1:]:
            # if the start is greater than the previous end
            if start >= prevEnd:
                # have the previous end equal this new end. They dont overlap
                prevEnd = end
            else:
                # else, increment the count by 1 since we have an element that overlaps
                res += 1
                # update the previous end to the minimum between this end and the previous end
                prevEnd = min(end, prevEnd)
        return res
