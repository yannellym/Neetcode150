
Code

Testcase
Testcase
Result

252. Meeting Rooms
Solved
Easy
Topics
Companies
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

Example 1:

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True

        intervals.sort()
   
        x,y = intervals[0][0], intervals[0][1]

        for a, b in intervals[1:]:
            if a < y:
                return False
            y = b
        return True
