# 1456. Maximum Number of Vowels in a Substring of Given Length
# Medium
# 2.5K
# 80
# Companies
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length
# Accepted
# 127.6K
# Submissions
# 214.8K
# Acceptance Rate
# 59.4%

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """ 
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        max_vowels = 0
        curr_vowels = 0
        for i in range(len(s)):
            if i >= k and s[i-k] in vowels:
                curr_vowels -= 1
            if s[i] in vowels:
                curr_vowels += 1
            max_vowels = max(max_vowels, curr_vowels)
            
        return max_vowels
