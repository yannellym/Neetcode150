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
(known limitations)
1	def isValid(s):
2	    stack = []
3	    brackets_mapping = {
4	        ')': '(',
5	        '}': '{',
6	        ']': '[',
7	    }
8	        
9	    for bracket in s:
10	        if bracket not in brackets_mapping:
11	            stack.append(bracket)
12	        elif stack and stack[-1] == brackets_mapping[bracket]:
13	            stack.pop()
14	        else:
15	            return False
16	        
17	    return len(stack) == 0
18	    
19	isValid("((()(())))")
