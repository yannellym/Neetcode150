1137. N-th Tribonacci Number
Solved
Easy
Topics
Companies
Hint
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
Seen this question in a real interview before?



class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        
        # Initialize tribonacci sequence with base cases
        tribonacci_seq = [0, 1, 1]
        
        # Generate tribonacci sequence iteratively
        for i in range(3, n + 1):
            tribonacci_seq.append(tribonacci_seq[i - 1] + tribonacci_seq[i - 2] + tribonacci_seq[i - 3])
        print( tribonacci_seq)
        return tribonacci_seq[n]
