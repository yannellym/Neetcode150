# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

 

# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:

# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
# Example 3:

# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # ugly numbers cannot be negative
        if n <= 0:
            return False

        for p in [2,3,5]:
            # while n can be divided cleanly by any of these numbers
            while n % p == 0:
                # divide it by the number and update n
                n = n // p
                # this will make the number smaller continously
                # once it cannot be divided by n, it will move on to the next p
        # at the end, we can check if n = 1. 
        #If it equals one, it is an ugly number because it was divisible by 2,3,5
        # if it equals something different, it means it has other prime divisors.
        return n == 1
# https://www.youtube.com/watch?v=M0Zay1Qr9ws&ab_channel=NeetCode
