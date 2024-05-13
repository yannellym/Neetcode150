907. Sum of Subarray Minimums
Solved
Medium
Topics
Companies
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
Seen this question in a real interview before?
1/5

class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        stack = []

        arr = [0] + arr + [0]
        res = 0

        for i, num in enumerate(arr):
            # if our current index at the top of the stack is looked up in arr
            # and that number in arr is greater than the number we currently have
            while stack and arr[stack[-1]] > num:
                # pop the top of the stack
                j = stack.pop()
                # reference the new top of the stack
                k = stack[-1]
                # our new res will be:
                # res + the number in arr that's in index j
                # *  (our current index - j) * (j - k) 
                # % MOD
                res = ( res + arr[j] * (i-j) * (j-k) ) %  MOD
            
            stack.append(i)
        return res
