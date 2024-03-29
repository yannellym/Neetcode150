# 973. K Closest Points to Origin
# Medium
# 7.1K
# 259
# Companies
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

# Example 1:


# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

# Constraints:

# 1 <= k <= points.length <= 104
# -104 < xi, yi < 104
# Accepted
# 947.6K
# Submissions
# 1.4M
# Acceptance Rate
# 65.8%

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # first, we create a list that will be our temp minHeap
        minHeap = []
        # second, create a list to add our answers
        res = []
        # for every x,y point in points
        for x, y in points:
            # square both and add them together, this will equal the distance
            distance = (x**2) + (y**2)
            # to the minHeap, append an array with 3 values: distance, x, and y.
            minHeap.append([distance, x, y])
        # heapify our minHeap temp
        heapq.heapify(minHeap)

        # while our k value is greater than 0
        while k > 0:
            # extract the distance , x, y when you pop from the heap
            distance, x, y = heapq.heappop(minHeap)
            # append the x,y coordinate to the res
            res.append([x,y])
            # decrement k
            k -= 1
        # at the end, you should have a list of coordinates according to their 
        # min squared values
        return res
#alternative

import heapq
import math


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # create the heap
        heap = []
        # heapify it
        heapq.heapify(heap)
        # set our origin values 
        x2 = 0
        y2 = 0

        # for every x,y value in points
        for x1,y1 in points:
            # compute the euclidian distance
            value = math.sqrt((((x1 - x2)**2) + ((y1 - y2)**2)))
            # add a tuple of the square root value and the points to the heap
            heapq.heappush(heap, (value, [x1,y1]))
        # our res array
        res = []
        # for the length of k
        for i in range(k):
            # get the first value from the heap, and the value at index 1, and pop it
            sub = heapq.heappop(heap)[1]
            # append it to the sub
            res.append(sub)
        
        return res
            
