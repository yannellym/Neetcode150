# 1935. Maximum Number of Words You Can Type
# Easy
# 444
# 21
# Companies
# There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

# Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

 

# Example 1:

# Input: text = "hello world", brokenLetters = "ad"
# Output: 1
# Explanation: We cannot type "world" because the 'd' key is broken.
# Example 2:

# Input: text = "leet code", brokenLetters = "lt"
# Output: 1
# Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
# Example 3:

# Input: text = "leet code", brokenLetters = "e"
# Output: 0
# Explanation: We cannot type either word because the 'e' key is broken.
 

# Constraints:

# 1 <= text.length <= 104
# 0 <= brokenLetters.length <= 26
# text consists of words separated by a single space without any leading or trailing spaces.
# Each word only consists of lowercase English letters.
# brokenLetters consists of distinct lowercase English letters.
# Accepted
# 41.6K
# Submissions
# 58.2K
# Acceptance Rate

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """

        bkLetters = list(brokenLetters)
        words = text.split(" ")
        n = len(words)
        for sub in words:
            l = False
            for letter in bkLetters:
                if letter in sub:
                    l = True
            if l == True:
                n-=1
        return n

# 71.4%
