# 1968. Array With Elements Not Equal to Average of Neighbors
# Medium
# 444
# 32
# Companies
# You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.

# More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

# Return any rearrangement of nums that meets the requirements.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: [1,2,4,5,3]
# Explanation:
# When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
# When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
# When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.
# Example 2:

# Input: nums = [6,2,0,9,7]
# Output: [9,7,6,2,0]
# Explanation:
# When i=1, nums[i] = 7, and the average of its neighbors is (9+6) / 2 = 7.5.
# When i=2, nums[i] = 6, and the average of its neighbors is (7+2) / 2 = 4.5.
# When i=3, nums[i] = 2, and the average of its neighbors is (6+0) / 2 = 3.
 

# Constraints:

# 3 <= nums.length <= 105
# 0 <= nums[i] <= 105
# Accepted
# 24.4K
# Submissions
# 49.5K
# Acceptance Rate
# 49.3%

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # iterate through nums starting at 1, and through len of nums-1
        for i in range(1, len(nums)-1):
            # check if the curr num is less than the one on the right, if so, swap it
            if nums[i-1] < nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                # if the num on the right is less than the current, swap it
            elif nums[i+1] < nums[i] <nums[i-1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        print(nums) # -- > [1, 3, 2, 5, 4]
        return nums
