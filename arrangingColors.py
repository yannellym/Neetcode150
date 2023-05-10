# 441. Arranging Coins
# Easy
# 3.3K
# 1.2K
# Companies
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

 

# Example 1:


# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:


# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
 

# Constraints:

# 1 <= n <= 231 - 1
# Accepted
# 357.1K
# Submissions
# 771.6K
# Acceptance Rate
# 46.3%


# Approach
# Initialize two pointers left and right to 1 and n, respectively.
# While left <= right, compute the midpoint mid between left and right.
# Compute the total number of coins required to build mid complete rows using the formula (mid * (mid + 1)) // 2.
# If the total number of coins is greater than or equal to n, set right to mid - 1 (i.e., look for a smaller number of rows that use fewer coins).
# Otherwise, set left to mid + 1 (i.e., look for a larger number of rows that use more coins).
# Return right as the answer.
# Complexity
# Time complexity:
# Space complexity:
# Code
class Solution:
    def arrangeCoins(self, n):
        # Initialize pointers to first and last possible row lengths
        left, right = 1, n
        
        while left <= right:
            # Compute the midpoint between left and right
            #It is an optimized way to avoid integer overflow when left and right are large integers, by first computing the difference between right and left and then adding half of it to left.
            mid = left + (right - left) // 2
            
            # Compute the total number of coins needed for mid complete rows
            coins = (mid * (mid + 1)) // 2
            
            # If we have enough coins, look for a smaller number of rows
            if coins <= n:
                left = mid + 1
            # Otherwise, look for a larger number of rows
            else:
                right = mid - 1
                
        # Return the number of complete rows (i.e., right pointer)
        return right
      
      
      
      
   # o(n) solution:
      
      class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        i = 1

        while n>0:
            res += i
            i+=1
            n-=i
        return i-1
