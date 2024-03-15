https://leetcode.com/problems/binary-subarrays-with-sum/
930. Binary Subarrays With Sum
Solved
Medium
Topics
Companies
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
 

Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
Seen this question in a real interview before?



class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        count = 0
        sum_freq = {0: 1}  # Dictionary to store frequency of sums
        curr_sum = 0

        for num in nums:
            curr_sum += num
            print(sum_freq)
            # Check if there exists a previous prefix sum such that the difference is equal to the goal
            count += sum_freq.get(curr_sum - goal, 0)
            # Update the frequency of the current sum
            sum_freq[curr_sum] = sum_freq.get(curr_sum, 0) + 1

        return count


