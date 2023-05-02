# 658. Find K Closest Elements
# Medium
# 6.9K
# 561
# Companies
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
 

# Constraints:

# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104
# Accepted
# 430.5K
# Submissions
# 919.2K


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        
        # initialize left and right pointers to the start and end of the input list
        left = 0
        right = len(arr) - 1
        
        # while the difference between the right and left pointers is greater than or equal to k
        while right - left >= k:
            # compare the absolute differences between x and the elements at the left and right pointers
            if abs(x - arr[left]) > abs(x - arr[right]):
                # increment the left pointer if the difference between x and the element at the left pointer is greater
                left += 1
            else:
                # decrement the right pointer if the difference between x and the element at the right pointer is greater
                right -= 1
        
        # return the sublist of arr starting from the left pointer and ending at the right pointer, which contains the k closest elements
        return arr[left:right+1]
