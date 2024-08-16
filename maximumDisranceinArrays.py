624. Maximum Distance in Arrays
Solved
Medium
Topics
Companies
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

 

Example 1:

Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Example 2:

Input: arrays = [[1],[1]]
Output: 0
 

Constraints:

m == arrays.length
2 <= m <= 105
1 <= arrays[i].length <= 500
-104 <= arrays[i][j] <= 104
arrays[i] is sorted in ascending order.
There will be at most 105 integers in all the arrays.


class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        # Initialize with the first array's first and last elements
        min_value = arrays[0][0]
        max_value = arrays[0][-1]
        max_distance = 0
        
        # Iterate through each array starting from the second
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            
            # Calculate the maximum distance considering the current array's min and max
            max_distance = max(max_distance, abs(max_value - current_min), abs(current_max - min_value))
            
            # Update the global min_value and max_value
            min_value = min(min_value, current_min)
            max_value = max(max_value, current_max)
        
        return max_distance
