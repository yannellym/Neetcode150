905. Sort Array By Parity
Solved
Easy
Topics
Companies
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
Accepted
695.9K
Submissions
915.2K
Acceptance Rate
76.0%


class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        l = 0
        r = len(nums)-1


        for i in range(len(nums)):

            if nums[i] % 2 == 0:
                res[l] = nums[i]
                l +=1
            else:
                res[r] = nums[i]
                r -=1
        return res
# alternative 

left, right = 0, len(nums) - 1
    
    while left < right:
        if nums[left] % 2 == 1 and nums[right] % 2 == 0:
            nums[left], nums[right] = nums[right], nums[left]  # Swap odd and even elements
            left += 1
            right -= 1
        elif nums[left] % 2 == 0:
            left += 1
        else:
            right -= 1
    
    return nums
