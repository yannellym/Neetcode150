# 39. Combination Sum
# Solved
# Medium
# Topics
# Companies
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
 

# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
# Accepted
# 1.6M
# Submissions
# 2.3M
# Acceptance Rate
# 69.9%


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []  # Initialize a list to store valid combinations
        
        def findComb(i, curr, total):
            # Base case: If the current total equals the target, a valid combination is found
            if total == target:
                res.append(curr[:])  # Make a copy of curr and append it to the result list
                return 
            
            # Base case: If the current index exceeds the candidates list length or total exceeds the target, return
            if i >= len(candidates) or total > target:
                return

            # Include the current candidate in the current combination
            curr.append(candidates[i])

            # Recursively explore combinations with the current candidate included
            findComb(i, curr, total + candidates[i])

            # Backtrack by removing the last added candidate to explore combinations without it
            curr.pop()

            # Recursively explore combinations without the current candidate
            findComb(i + 1, curr[:], total)  # Make a copy of curr and pass it to the next recursive call

        # Start the recursion with initial values
        findComb(0, [], 0)

        return res


# backtracking 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                # If target is reached, add the current combination to the result
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                # Explore the combination with the current candidate
                print(f"Exploring: {path + [candidates[i]]}")
                backtrack(i, target - candidates[i], path + [candidates[i]])
                print(f"Backtrack from: {path + [candidates[i]]}")

        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result
        
