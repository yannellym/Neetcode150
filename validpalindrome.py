# 125. Valid Palindrome
# Easy

# 4789

# 5946

# Add to List

# Share
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution(object):
    def isPalindrome(self, s):
        # i starts at beginning of s and j starts at the end         
        i, j = 0, len(s) - 1
        # While i is still before j        
        while i < j:
            # If i is not an alpha-numeric character then advance i            
            if not s[i].isalnum():
                i += 1
            # If j is not an alpha-numeric character then advance i
            elif not s[j].isalnum():
                j -= 1
            # Both i and j are alpha-numeric characters at this point so if they do not match return the fact that input was non-palendromic
            elif s[i].lower() != s[j].lower():
                return False
            # Otherwise characters matched and we should look at the next pair of characters
            else:
                i, j = i + 1, j - 1
        # The entire stirng was verified and we return the fact that the input string was palendromic         
        return True
