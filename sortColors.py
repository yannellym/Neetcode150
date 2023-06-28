# 75. Sort Colors
# Medium

# 13013

# 477

# Add to List

# Share
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.


# more fficient
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        i = 0

        while i <= r:
            # If nums[i] is 0, it is swapped with the element at index l, and both l and i are incremented.
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            # If nums[i] is 2, it is swapped with the element at index r, and r is decremented. 
            # the element at index i is not swapped because the value at r is not known yet 
            # and needs to be checked.
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            # If nums[i] is 1, i is simply incremented.
            else:
                i += 1
        

    '''
        In this part of the code, we're checking if the current element at index i in the nums array is 
        equal to 2. If it is, we perform a swap between the element at index i and the element at index r,
        and then we decrement the value of r by 1.

        The reason why we don't increment i after the swap is that the element at index i after the swap    is now an unknown value. It could be a 0, 1, or 2 that was previously at index r, so we need to     re-evaluate this new element before moving to the next iteration.

        By swapping the element at index i with the element at index r, we effectively move the current 2 towards the end of the array. After the swap, the element originally at index r is now at index i. We then decrement r by 1 to ensure that the next 2, if any, will be placed correctly towards the end of the array.
    '''




# alternative 

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) -1 
        i = 0

        def swap(index, digit ):
            tmp = nums[index]
            nums[index] = nums[digit]
            nums[digit] = tmp

        # this will make sure to iterate through each num
        # without repeating it 
        while i <= right:
            # if the number at the ith index is 0, swap it with  the num on the left
            # increase the left
            if nums[i] == 0:
                swap(left, i)
                left += 1
            # if the number at the ith index is 2, swap it with the num on the right
            # decrease the right
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
                # this is so i can cancel out when we increase it in the following line
                # you dont accidently replace the left numbers with the right ones
                i -= 1
            i += 1
