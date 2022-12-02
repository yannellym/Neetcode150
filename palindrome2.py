# 680. Valid Palindrome II
# Easy

# 6594

# 337

# Add to List

# Share
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# Accepted
# 560,500
# Submissions
# 1,425,251



class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        
        # while index i is less than index j
        while i < j:
            # if char at i doesnt equal char at j
            if s[i] != s[j]:
                # skip the left char and save the string
                left_replaced = s[i+1:j+1]
                # skip the right char and save the string
                right_replaced = s[i:j]
                # if the string equals to s reversed, return true because we made one replacement
                # else return false because itll require more than 1 replacement
                if (left_replaced == left_replaced[::-1]) or (right_replaced == right_replaced[::-1]):
                    return True
                else:
                    return False
            # increase the pointers so you go through the string   
            i += 1
            j -= 1
        #return true if the code above doesnt executive because this means the entire string
        # if a palindrome
        return True
                
