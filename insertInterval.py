# 57. Insert Interval
# Medium
# 7.6K
# 525
# Companies
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

 

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105
# Accepted
# 700.6K
# Submissions
# 1.8M
# Acceptance Rate
# 38.8%


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        # declare an array for our results
        res = []

        # loop ith amount of times, with i being the length of intervals
        for i in range(len(intervals)):
            # if the newInterval comes before the first subarray in intervals
            # append the newInterval to the res
            # return res plus the rest of the intervals array
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # else if the newinterval digit at position 0 is greater than
            # the current interval's diigit at position 1
            # append the subarray to the res
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # get the minimum between the intervals's digit at index 0 
                # and the sub array's digit at index 0
            # get max between the intervals's digit at index 1 
                # and the sub array's digit at index 1
            # set the newinterval to equal the min and max obtained above
             # we can't add it to res yet because it might still overlap with other subarrays
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        # if we get to the end of the array and we still haven't added the new interval
         # this means that it didnt overlap with any of the subarrays. Just add it
        res.append(newInterval)
        # return the res
        return res
            
