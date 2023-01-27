# 20. Valid Parentheses
# Easy
# 17.7K
# 982
# Companies
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
# 3M
# Submissions
# 7.4M
# Acceptance Rate
# 40.4%



class Solution:
    def isValid(self, s: str) -> bool:
        # build a dictionary that contains all the brackets and their partners
        store = { 
        ')':'(',
        ']':'[',
        '}':'{'
        }
        # set a stack to keep track of our brackets and their partners
        stack = []
        # for every symbol is s:
        for sym in s:
            # if the symbol is in the store:
            if sym in store:
                # if there is a stack and the last item in the stack if the partner of this symbol:
                if stack and store[sym] == stack[-1]:
                    # pop it because it has a partner
                    stack.pop()
                else:
                    # if no partner, return False, there are no even pairs
                    return False
            else:
                # if its not in the store, it must be a partner symbol
                # append it to the stack
                stack.append(sym)
        # if we get here and our stack is greater than 0, it means some of our symbol didnt have a partner
        if len(stack) > 0:
            # return false as there are some symbols left in our stack
            return False
        # if everything above executes correctly, return true because we have even pairs of our symbols
        return True
