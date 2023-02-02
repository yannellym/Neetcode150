# 394. Decode String
# Medium
# 10.3K
# 457
# Companies
# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
 

# Constraints:

# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].
# Accepted
# 611.5K
# Submissions
# 1.1M


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        # will loop as much as the amount of letters in s
        for i in range(len(s)):
            # if the char doesnt equal a closing brack, append it to the stack
            if s[i] != "]":
                stack.append(s[i])
            else:
                # temp variable to hold our temp string
                substr = ""
                # while the top of the stack doesnt equal a beginning bracket
                while stack[-1] != '[':
                    # have the substr equal the popped value from the stack plus the substr
                    # this will prevent the string from being reversed
                    substr = stack.pop() + substr
                # make sure to pop the beginning bracket
                stack.pop()

                # variable for the numbers we will encounter
                num = ""
                # while there is a stack, and the top of the stack is a digit
                while stack and stack[-1].isdigit():
                    # have the num variable equal the char from top of the stack plus num itself
                    # this will prevent the string from being reversed
                    num = stack.pop() + num
                # append the entire multiplication of num and the substring to the stack
                stack.append(int(num) * substr)
        # the stack contains an array of words, make sure to join them at the end
        return ''.join(stack)



            
            
