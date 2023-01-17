# 844. Backspace String Compare
# Easy
# 6K
# 275
# Companies
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
 

# Constraints:

# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
 

# Follow up: Can you solve it in O(n) time and O(1) space?


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return the result of calling these two functions
        return self.backspace(s) == self.backspace(t) 

    #create a helper function and pass in the string
    def backspace(self, n):
        # create a stack that will help us keep track of the chars
        store = []
        # for every char in n
        for char in n:
            # if the char doesnt equal #
            if char != "#":
                # append it to the char
                store.append(char)
            # else if there is a store, pop from it
            elif store:
                store.pop()
        # return the stack
        return store
