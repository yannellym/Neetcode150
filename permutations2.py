47. Permutations II
Solved
Medium
Topics
Companies
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
Accepted
833.8K
Submissions
1.4M
Acceptance Rate
58.1%

lass Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        # if the length of the array is 1, it only has one permutation so return
        if len(nums) == 1:
            return [nums[:]]

        # iterate through the nums array
        for i in range(len(nums)):
            # pop the first value
            selected  = nums.pop(0)
            # get the permuations for every single element in nums
            permutations = self.permuteUnique(nums)
            # for every single permutation, add the selected number.
            for perm in permutations:
                perm.append(selected)
                # if the permutation is not in res (meaning that it is unique)
                if perm not in res:
                    res.append(perm)
            # clean up and make sure to append the popped(selected) value back to the nums array
            nums.append(selected)
        return res


# efficient 
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])  # Append a copy of the current permutation
                return

            for i in range(start, len(nums)):
                # Skip duplicates to avoid duplicate permutations
                if i != start and nums[i] == nums[start]:
                    continue

                nums[start], nums[i] = nums[i], nums[start]  # Swap elements
                backtrack(start + 1)  # Recursively generate permutations
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack (restore original order)

        nums.sort()  # Sort the input to handle duplicates
        res = []
        backtrack(0)
        return res
      
 
