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

# simple solution
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        merged = []
        i, n = 0, len(intervals)
        # Add all intervals ending before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        # Merge all intervals that overlap with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        merged.append(newInterval)
        # Add all intervals starting after newInterval ends
        while i < n:
            merged.append(intervals[i])
            i += 1
        return merged

# clever solution

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        merged = []
        i, n = 0, len(intervals)
        # Add all intervals ending before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        # Merge all intervals that overlap with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        merged.append(newInterval)
        # Add all intervals starting after newInterval ends
        while i < n:
            merged.append(intervals[i])
            i += 1
        return merged



# new documentation

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """


        res = []

        # iterate through every sub in intervals
        for sub in range(len(intervals)):
            # if the new interval's[1] is < than intervals[sub][1] just add the new interval to the res 
            # and return res + intervals after this current one 
            if newInterval[1] < intervals[sub][0]:
                res.append(newInterval)
                return res + intervals[sub:]
            # else if the newInterval's 0 is greater than intervals sub 1, just append to the res
            elif newInterval[0] > intervals[sub][1]:
                res.append(intervals[sub])
            # else, take the min and max between both
            else:
                newInterval = [min(newInterval[0], intervals[sub][0]), max(newInterval[1], intervals[sub][1])]
        # dont forget to append the newinterval in case the func above didnt executre
        res.append(newInterval)
        return res
       

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
            
