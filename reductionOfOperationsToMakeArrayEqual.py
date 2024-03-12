1887. Reduction Operations to Make the Array Elements Equal
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:

Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
Reduce nums[i] to nextLargest.
Return the number of operations to make all elements in nums equal.

 

Example 1:

Input: nums = [5,1,3]
Output: 3
Explanation: It takes 3 operations to make all elements in nums equal:
1. largest = 5 at index 0. nextLargest = 3. Reduce nums[0] to 3. nums = [3,1,3].
2. largest = 3 at index 0. nextLargest = 1. Reduce nums[0] to 1. nums = [1,1,3].
3. largest = 3 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,1].
Example 2:

Input: nums = [1,1,1]
Output: 0
Explanation: All elements in nums are already equal.
Example 3:

Input: nums = [1,1,2,2,3]
Output: 4
Explanation: It takes 4 operations to make all elements in nums equal:
1. largest = 3 at index 4. nextLargest = 2. Reduce nums[4] to 2. nums = [1,1,2,2,2].
2. largest = 2 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,1,2,2].
3. largest = 2 at index 3. nextLargest = 1. Reduce nums[3] to 1. nums = [1,1,1,1,2].
4. largest = 2 at index 4. nextLargest = 1. Reduce nums[4] to 1. nums = [1,1,1,1,1].
 
class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        up = 0
        
        for i in range(1, len(nums)):
            print(nums[i], nums[i - 1])
            if nums[i] != nums[i - 1]:
                up += 1
                
            ans += up
        
        return ans

        '''Sorting: Sort the input list nums in ascending order.
         After sorting, nums becomes [1, 3, 5].

        Initialization: Set ans = 0 and up = 0.

        Loop Iteration 1 (i = 1):

        Current element: nums[1] = 3, Previous element: nums[0] = 1.
        Since they are not equal, increment up by 1 (up = 1).
        Add the current value of up to ans (ans = 0 + 1 = 1).
        Loop Iteration 2 (i = 2):

        Current element: nums[2] = 5, Previous element: nums[1] = 3.
        Since they are not equal, increment up by 1 (up = 2).
        Add the current value of up to ans (ans = 1 + 2 = 3).
        Return: Return ans, which is 3.
        '''
