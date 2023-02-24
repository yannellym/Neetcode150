# 20. Valid Parentheses
# Easy

# 15532

# 771

# Add to List

# Share
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
# Accepted
# 2,632,293
# Submissions
# 6,457,247


Python 3.6


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # a stack to easily pop our values
        stack = []
        # keeps track of the closing/opening bracket
        store = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        
        # for every symbol in s
        for symbol in s:
            # if the symbol is not in the store, 
            # it means we have an opening bracket
            # we can append the symbol to the stack
            if symbol not in store:
                stack.append(symbol)
            # if there's a stack AND the last item in the stack
            # is the opening bracket of this symbol
            elif stack and stack[-1] == store[symbol]:
                # pop it from the stack as we have a match
                stack.pop()
            else:
                # if theres no stack and the matching bracket 
                # is not in the store, just return false
                return False
        # verify that the length of the stack is 0,
        # this will mean its empty and we can return true
        return len(stack) == 0
