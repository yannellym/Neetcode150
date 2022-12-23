# 3. Longest Substring Without Repeating Characters
# Medium

# 28967

# 1234

# Add to List

# Share
# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = set()
        
        left = 0
        res = 0
        # for every character in the string s
        for r in range(len(s)):
            # while char at position r is in the window
            while s[r] in window:
                # remove the char on the left
                window.remove(s[left])
                # update the left index
                left += 1
            # add the new char to the window
            window.add(s[r])
            # choose the max window size between the res, and the window length
            res = max(res, r - left + 1)
        return res
                
