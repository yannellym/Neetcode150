# 338. Counting Bits
# Easy
# 9.2K
# 442
# company
# Amazon
# company
# Adobe
# company
# Goldman Sachs
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 

# Constraints:

# 0 <= n <= 105
 

# Follow up:

# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
# Accepted
# 816.8K
# Submissions
# 1.1M
# Acceptance Rate
# 76.2%


class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Initialize the result array with 0's
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            # The number of 1's in i is equal to the number of 1's in i // 2 (right-shift by 1 bit)
            #  plus the last bit of i.
            ans[i] = ans[i >> 1] + (i & 1)

        return ans



# i >> 1: Right-shift i by 1 bit, which is equivalent to dividing i by 2 and discarding any fractional part. This gives the number obtained by removing the least significant bit from i.




# i & 1: Perform a bitwise AND operation between i and 1. This extracts the least significant bit of i, which is either 0 or 1.

    # Suppose i = 13, which is represented in binary as 1101. To understand the result of i & 1, we perform a   
    # bitwise AND operation between i and the binary number 1 (0b0001):

    # i =  1101 (binary)
    # &     0001 (binary)
    # -----------
    #       0001 (binary)   --> Result: 1
    # As you can see, the result of the bitwise AND operation is 0001 in binary, which is equal to 1 in decimal. 
    # This indicates that the least significant bit of i is 1. Therefore, i & 1 extracts the last bit of i,
    #  which is 1

#     Suppose we are iterating through the loop with n = 5. The initial ans array is [0, 0, 0, 0, 0, 0].

# When i = 1:

# i = 0b0001, i >> 1 = 0b0000 (right-shift by 1).
# ans[i >> 1] will be ans[0b0000], which is ans[0]. Since ans[0] is initialized as 0, ans[1] will remain 0.
# When i = 2:

# i = 0b0010, i >> 1 = 0b0001 (right-shift by 1).
# ans[i >> 1] will be ans[0b0001], which is ans[1]. We already calculated ans[1] in the previous iteration, and it is 1. So, ans[2] will be 1.
# When i = 3:

# i = 0b0011, i >> 1 = 0b0001 (right-shift by 1).
# ans[i >> 1] will be ans[0b0001], which is ans[1]. As mentioned before, ans[1] is 1. So, ans[3] will be 1 + 1 = 2.
# When i = 4:

# i = 0b0100, i >> 1 = 0b0010 (right-shift by 1).
# ans[i >> 1] will be ans[0b0010], which is ans[2]. We already calculated ans[2] earlier, and it is 1. So, ans[4] will be 1.
# When i = 5:

# i = 0b0101, i >> 1 = 0b0010 (right-shift by 1).
# ans[i >> 1] will be ans[0b0010], which is ans[2]. As stated before, ans[2] is 1. So, ans[5] will be 1 + 1 = 2.
# After completing the loop, the final ans array will be [0, 1, 1, 2, 1, 2], which matches the output for n = 5 as given in the problem statement.

