342. Power of Four
Solved
Easy
Topics
Companies
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?
Accepted
582.5K
Submissions
1.2M
Acceptance Rate
47.5%

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and log(n, 4) % 1 == 0
        
        '''
        This works because, when n is a power of 4, its logarithm with base 4 will be an integer. For example:

        4^0 = 1, log(1, 4) = 0
        4^1 = 4, log(4, 4) = 1
        4^2 = 16, log(16, 4) = 2
        4^3 = 64, log(64, 4) = 3
        And so on...
        In all of these cases, log(n, 4) results in an integer, so log(n, 4) % 1 is equal to 0.
        However, if n is not a power of 4, then log(n, 4) will result in a non-integer value,
        and log(n, 4) % 1 will not equal 0, causing the function to return False

        '''



class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # log solution 
        if n <=0:
            return False
        else:
            return n>0 and log(n,4).is_integer()  

        # alternative recursive solution
        # if n == 1:
        #     return True
        # if n <= 0 or n%4:
        #     return False
        # return self.isPowerOfFour(n//4)
