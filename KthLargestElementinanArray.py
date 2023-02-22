# 215. Kth Largest Element in an Array
# Medium
# 13.2K
# 656
# Companies
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# You must solve it in O(n) time complexity.

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104
# Accepted
# 1.7M
# Submissions
# 2.5M
# Acceptance Rate
# 66.0%
#



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # convert all the numbers to negatives
        for i in range(len(nums)):
            nums[i] = -nums[i]
        #  convert the array into a heapq
        heapq.heapify(nums)
        # loop through the heapq, k -1 amount of times
        for i in range(k-1):
            # this will pop all the k-1 largest elements
            x =  heapq.heappop(nums)
            print(x)
        # the heap will end up witht he element we want at the end,
        # its negative so we have to turn it positive
        return -heapq.heappop(nums)
