# 1929. Concatenation of Array
# Easy

# 1392

# 221

# Add to List

# Share
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

 

# Example 1:

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
# Example 2:

# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]
 

# Constraints:

# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000
# Accepted
# 248,205
# Submissions
# 271,155

class Solution(object):
    def getConcatenation(self, nums):
        store = nums
        store.extend(nums)
        return store

     
# better solution
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # the length of nums
        n = len(nums)
        # array of 2n length
        store = [0] * (n*2)

        # l will start at 0 and r will start at n
        l = 0
        r = n

        # for every integer in nums
        for i in nums:
            # store the interger in store[l] and store[r]
            store[l] = i
            store[r] = i
            # increase the pointers
            l+=1
            r+=1
        return store

    # another solution
    
    class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # the length of nums
        n = len(nums)
        # array of 2n length
        store = [0] * (n*2)

        # l will start at 0 
        l = 0

        # for every integer in nums
        for i in nums:
            # store the interger in store[l] and store[r]
            store[l] = i
            store[l+n] = i
            # increase the pointer
            l += 1
        return store
