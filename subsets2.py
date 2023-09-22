
Code

Testcase
Testcase
Result

90. Subsets II
Solved
Medium
Topics
Companies
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
Accepted
783.3K
Submissions
1.4M
Acceptance Rate
56.5%
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [ [] ]

        for num in nums:
            for j in range(len(res)):
                sub = sorted([num] + res[j])
                if sub not in res:
                    res.append(sub)
        return res
        
