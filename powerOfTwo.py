231. Power of Two
Solved
Easy
Topics
Companies
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
 

Constraints:

-231 <= n <= 231 - 1
 class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n is less than or equal to 0, return False
        # negative numbers can;t be a power of two
        if n <= 0:
            return False
        # while n is greater than 1
        while n > 1:
            # check if the number can be cleanly divisible by two
            if n % 2 != 0:
                # if not divisiblee, its not a power of two. Return false
                return False
            # if its divisible, halve n and continue loop
            n /= 2
        # if we have exited the loop, return True as its a power of two,
        return True

        '''
        Since � = 16 n=16 is positive, the process proceeds by entering a loop because � > 1 n>1.
        It checks if � n is divisible by 2, which is the case since 16 % 2 = 0 16%2=0, indicating 
        divisibility by 2. � n is then updated by dividing it by 2, resulting in � = 16 / 2 = 8 n=16/
        2=8. This process is repeated, checking divisibility by 2 for each updated value of � n, 
        until � n reaches 1. Once � n becomes 1, the loop exits. Since � n has reached 1, the 
        function returns True, confirming that 16 is indeed a power of two according to the provided 
        approach.
        '''

