# 287. Find the Duplicate Number
# Medium
# 19.2K
# 2.9K
# company
# Adobe
# company
# Amazon
# company
# Microsoft
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
 

# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

# Follow up:

# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?
# Accepted
# 1.2M
# Submissions
# 2M
# Acceptance Rate
# 59.1%



class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[0]
    
        # Move slow and fast pointers to find the meeting point
        while True:
            #print("Slow:", slow, "Fast:", fast)
            slow = nums[slow]
            
            fast = nums[nums[fast]]
            #print("advanced Fast:", fast)
            # meeting points where they intersect
            if slow == fast:
                break
        
        # Reset slow to the start and find the duplicate number
        slow = nums[0]
        while slow != fast:
            print("org Slow:", slow, "org Fast:", fast)
            slow = nums[slow]
            fast = nums[fast]
            print("Slow:", slow, "Fast:", fast)
        
        return slow

#         Initialize two pointers, slow and fast, to the first element of the array.
# Move slow one step at a time and fast two steps at a time until they meet.
# Since there is a duplicate number, there must be a cycle in the array.
# The meeting point is guaranteed to be inside the cycle.
# Reset the slow pointer to the first element and keep the fast pointer at the meeting point.
# Move both pointers one step at a time until they meet again.
# The point at which they meet is the duplicate number.
