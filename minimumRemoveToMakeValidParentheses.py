# 1249. Minimum Remove to Make Valid Parentheses
# Medium
# 5.6K
# 103
# Companies
# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either'(' , ')', or lowercase English letter.
# Accepted
# 488.2K
# Submissions
# 742.2K
# Acceptance Rate
# 65.8%


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        # create a stack to temporarily save our values
        stack = []
        # the length of s
        N = len(s)
        # covert s to a list
        S = list(s)

        # loop N amount of times
        for i in range(N):
            # if s[i] equals an opening parenthesis
            if S[i] == "(":
                # append the index to the stack
                stack.append(i)
            # else if S[i] equals a closing parenthesis,
            elif S[i] == ")":
                # AND if there's a stack, pop the last val from the stack
                if stack:
                    stack.pop()
                # else, make S[i] equal ""
                else:
                    S[i] = ""
        # go through every letter in the stack
        for j in stack:
            # conver every index in S to ""
            S[j] = ""
        # join the letters of S together and return
        return "".join(S)
