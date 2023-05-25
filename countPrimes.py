# 204. Count Primes
# Medium
# 6.8K
# 1.3K
# company
# Capital One
# company
# Amazon
# company
# TikTok
# Given an integer n, return the number of prime numbers that are strictly less than n.

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0
 

# Constraints:

# 0 <= n <= 5 * 106
# Accepted
# 734.8K
# Submissions
# 2.2M
# Acceptance Rate
# 33.1%


import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
  
        
        if n <= 1:
            return 0

        primes = [True] * n  # Initialize a boolean list to mark primes
        primes[0] = False  # 0 is not prime
        primes[1] = False  # 1 is not prime

        i = 2

        while i < (n//2 + 1): # iterare only up to the square root of n
            if primes[i]: # if its marked as True in the primes array
                j = i * i  # Start marking multiples of i as non-prime from i * i
                while j < n: # while j is less than n
                    primes[j] = False  # Mark multiples of i as non-prime(False)
                    j += i  # Increment by i to get the next multiple of i (multiples of 2)
            i += 1  # Move to the next number

        return sum(primes)  # Count the number of primes

                
