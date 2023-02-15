# 77. Combinations
# Medium
# 5.7K
# 176
# Companies
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

 

# Example 1:

# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
# Example 2:

# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
 

# Constraints:

# 1 <= n <= 20
# 1 <= k <= n
# Accepted
# 639.8K
# Submissions
# 959K


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = []

        def backtrack(start, comb):
            # if the length of comb has reached the length needed(k)
            if len(comb) == k:
                # attach a copy of comb to the res
                # this is important because we dont want to modify comb 
                # when it is inside res
                res.append(comb[:])
                # return to exit
                return
            # loop n amount of times
            for i in range(start, n+1):
                # append the first num to comb
                comb.append(i)
                # recursively call backtrack on i+1, pass in comb
                backtrack(i+1, comb)
                # when all the recursive calls for the number have completed:
                # bob the first number you added
                comb.pop()
        # first, call backtrack func and pass in:
        # - the 1 as a start
        # [] as an initital placement for our combinations
        backtrack(1, [])
        return res
        

        # https://www.youtube.com/watch?v=q0s6m7AiM7o
