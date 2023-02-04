# 56. Merge Intervals
# Medium
# 17.9K
# 616
# Companies
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104
# Accepted
# 1.8M
# Submissions
# 3.9M
# Acceptance Rate
# 46.1%


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort the intervals array by the first value
        intervals = sorted(intervals)
        # the res array will include all of our final intervals
        # initialize the res array with the first subarray in intervals
        res = [intervals[0]]
        # for every start, end value in intervals[1:]
        for start, end in intervals[1:]:
            # get the last subarray in res, and get its value in index1
            lastEnd = res[-1][1]
            # if our current subarray's start value is less than or equal to 
            # res' last subarray value at index 1
            if start <= lastEnd:
                # replace the value of res' last subarray value at index 1 to be the max
                # bettern its last value and our current subarray's last value
                res[-1][1] =  max(lastEnd,end)
            else:
                # else, just append the current subarray
                res.append([start,end])
        return res
