# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

 

# Example 1:

# Input: nums = [1,4,3,2]
# Output: 4
# Explanation: All possible pairings (ignoring the ordering of elements) are:
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4.
# Example 2:

# Input: nums = [6,2,6,5,1,2]
# Output: 9
# Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
 

# Constraints:

# 1 <= n <= 104
# nums.length == 2 * n
# -104 <= nums[i] <= 104

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the list in ascending order
        nums.sort()
        # Initialize sum to zero
        max_sum = 0
        for i in range(0, len(nums), 2):
            # Add every element at even positions (0-indexed)
            max_sum += nums[i]
            
        return max_sum
      
      
# Time complexity: O(Nlog⁡N)O(N \log N)O(NlogN)

# Sorting the list nums of size 2⋅N2 \cdot N2⋅N will take O(2⋅Nlog⁡(2⋅N))O(2 \cdot N \log(2 \cdot N))O(2⋅Nlog(2⋅N)) time which is equivalent to O(Nlog⁡N)O(N \log N)O(NlogN), and iterating over the list will take an additional O(N)O(N)O(N) time. Hence, the time complexity is O(Nlog⁡N)O(N \log N)O(NlogN).

# Space complexity: O(N)O(N)O(N)

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        i = 0
        j = 1
        store = []

        # while j is less than the length of numbers
        while j < len(nums):
            # do a sliding window of 2 elements. Take the min of that window
            summ = min(nums[i:j+1])
            # add the min to a list
            store.append(summ)
            # increase both pointers to keep the window the same size
            j+=2
            i+=2
        # return the sum of all elements in the list
        return sum(store)
