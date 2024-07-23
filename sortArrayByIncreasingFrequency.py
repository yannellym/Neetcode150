sortclass Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        store = Counter(nums)
        # sort by the values in the store first, then by the keys in the store second
        # but sort the keys that are bigger first (that's why we have -. Ex -8 vs 2)
        nums.sort( key=lambda x:(store[x],-x))
        return nums
1636. Sort Array by Increasing Frequency
Solved
Easy
Topics
Companies
Hint
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
Seen this question in a real interview before?
1/5
Yes
No
Accepted
257.7K
Submissions
324.1K
