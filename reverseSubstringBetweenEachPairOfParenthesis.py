 def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for letter in s:
            if letter == ")":
                substr = []
                while stack and stack[-1] != "(":
                    substr.append(stack.pop())
                if stack:  # Remove the opening '(' from stack
                    stack.pop()
                # Reverse the collected substring and push back to stack
                stack.extend(substr)
            else:
                stack.append(letter)
        
        # Join all elements in the stack to form the final result
        return "".join(stack)


1190. Reverse Substrings Between Each Pair of Parentheses
Solved
Medium
Topics
Companies
Hint
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
 

Constraints:

1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.
