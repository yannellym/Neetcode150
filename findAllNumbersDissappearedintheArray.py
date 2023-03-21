# 448. Find All Numbers Disappeared in an Array
# Easy
# 8.2K
# 428
# Companies
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Accepted
# 708.9K
# Submissions
# 1.2M
# Acceptance Rate
# 59.9%

  nums.sort()
        store = set(nums)
        res = []

        for i in range(len(nums)):
            if i+1 not in store:
                res.append(i+1)
        return res
      
      
      
        # alternative

         # iterate through the input list and mark the values as visited
        for i in range(len(nums)):
            # get the absolute value of nums 1 and subtract one: THIS WILL TELL YOU THE INDEX IT SHOULD BE IN IN THE ARRAY
            index = abs(nums[i]) - 1
            # Mark that index in the array as negative: THIS IS HOW WE KNOW WE VISITED IT
            nums[index] = -abs(nums[index])
    
        # collect the missing values which are still positive
        missing = []
        # Iterate through i
        for i in range(len(nums)):
            # if nums i is greater than 0, this means we didnt visit it
            if nums[i] > 0:
                # append that value, plus + 1 to get the true number
                missing.append(i+1)
        
        return missing
