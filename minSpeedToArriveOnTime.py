https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/
Medium
2.1K
239
company
PhonePe
company
Google
You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.

 

Example 1:

Input: dist = [1,3,2], hour = 6
Output: 1
Explanation: At speed 1:
- The first train ride takes 1/1 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
- Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
- You will arrive at exactly the 6 hour mark.
Example 2:

Input: dist = [1,3,2], hour = 2.7
Output: 3
Explanation: At speed 3:
- The first train ride takes 1/3 = 0.33333 hours.
- Since we are not at an integer hour, we wait until the 1 hour mark to depart. The second train ride takes 3/3 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 2 hour mark. The third train takes 2/3 = 0.66667 hours.
- You will arrive at the 2.66667 hour mark.
Example 3:

Input: dist = [1,3,2], hour = 1.9
Output: -1
Explanation: It is impossible because the earliest the third train can depart is at the 2 hour mark.
 

Constraints:

n == dist.length
1 <= n <= 105
1 <= dist[i] <= 105
1 <= hour <= 109
There will be at most two digits after the decimal point in hour.
Accepted
84.6K
Submissions
178.1K
Acceptance Rate
47.5%

# class Solution(object):
#     def minSpeedOnTime(self, dist, hour):
#         """
#         :type dist: List[int]
#         :type hour: float
#         :rtype: int
#         """
      
#         # Helper function to check if it's possible to reach the office on time with given speed
#         def is_possible(speed):
#             total_time = 0
#             n = len(dist)
#             for i in range(n - 1):
#                 # Calculate the time taken for the current train ride with the given speed
#                 total_time += (dist[i] + speed - 1) // speed
#             # Calculate the time taken for the last train ride with the given speed
#             total_time += float(dist[-1]) / speed
#             return total_time <= hour

#         # Initialize binary search pointers and result variable
#         left = 1
#         right = 10**7  # The maximum possible speed, you can adjust this based on the problem constraints
#         res = -1

#         # Binary search to find the minimum speed required
#         while left <= right:
#             mid = (left + right) // 2
#             if is_possible(mid):
#                 # If it's possible to reach the office on time with the current speed,
#                 # update the result and search for smaller speeds in the left half
#                 res = mid
#                 right = mid - 1
#             else:
#                 # If it's not possible to reach the office on time with the current speed,
#                 # search for larger speeds in the right half
#                 left = mid + 1

#         return res
