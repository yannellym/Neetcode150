A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

 

Example 1:

Input: nums = [0,1,0,1,1,0,0]
Output: 1
Explanation: Here are a few of the ways to group all the 1's together:
[0,0,1,1,1,0,0] using 1 swap.
[0,1,1,1,0,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.
Example 2:

Input: nums = [0,1,1,1,0,0,1,1,0]
Output: 2
Explanation: Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.
Example 3:

Input: nums = [1,1,0,0,1]
Output: 0
Explanation: All the 1's are already grouped together due to the circular property of the array.
Thus, the minimum number of swaps required is 0.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

  https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/?envType=daily-question&envId=2024-08-02


class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Count the total number of 1's in the array
        total_ones = sum(nums)
        
        # If there are no 1's or only 1's, no swaps are needed
        if total_ones == 0 or total_ones == len(nums):
            return 0
        
        n = len(nums)
        
        # Step 2: Initialize the sliding window
        current_ones = sum(nums[:total_ones])
        max_ones_in_window = current_ones
        
        # Slide the window across the array using modulo to handle circular nature
        for i in range(1, n):
            # Remove the element going out of the window and add the new element coming into the window
            current_ones -= nums[i - 1]
            current_ones += nums[(i + total_ones - 1) % n]
            
            # Update the maximum number of 1's in any window
            max_ones_in_window = max(max_ones_in_window, current_ones)
        
        # Step 3: Calculate the minimum swaps
        min_swaps = total_ones - max_ones_in_window
        
        return min_swaps
