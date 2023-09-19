1288. Remove Covered Intervals
Solved
Medium
Topics
Companies
Hint
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1
 

Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= li < ri <= 105
All the given intervals are unique.
Accepted
112K
Submissions
197.5K
Acceptance Rate
56.7%



class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sort the intervals by the left most value first, then the right most value. 
        # the right most values will be sorted from biggest to smallest)
        intervals.sort(key=lambda i: (i[0], -i[1]))
        # we'll keep the first value from intervals as it wont be covered at first
        res = [intervals[0]] 

        # for every l and r value starting at index 1,
        for l, r in intervals[1:]:
            # get the prev values we set at res
            prevL, prevR = res[-1]
            # if a <= c and b >= d:
            if prevL <= l and prevR >= r:
                continue
            # append the new values to our res arr
            res.append([l,r])
        return len(res)



'''
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1

You have two intervals: [1,4] and [2,3].

The first interval [1,4] spans from 1 to 4 (inclusive on the left side, exclusive on the right side).

The second interval [2,3] spans from 2 to 3 (inclusive on the left side, exclusive on the right side).

In this case, the second interval [2,3] is indeed covered by the first interval [1,4] because:

The left endpoint of the second interval, 2, is greater than or equal to the left endpoint of the first interval, 1.
The right endpoint of the second interval, 3, is less than or equal to the right endpoint of the first interval, 4.
These conditions satisfy the correct criteria for one interval to be "covered" by another.

Since the second interval [2,3] is covered by the first interval [1,4], it is removed.

After removing the covered interval, you are left with only one interval, which is [1,4].

The function should return the number of remaining intervals, which is 1.

So, the output of this example is indeed 1 because there is only one remaining interval ([1,4]) after removing the covered interval ([2,3]), and this conforms to the correct condition for coverage.
'''
