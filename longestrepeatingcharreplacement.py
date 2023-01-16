# 424. Longest Repeating Character Replacement
# Medium

# 6466

# 253

# Add to List

# Share
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # set the longest_char variable to equal 0 initially
        longest_char = 0
        # win_start will be the start of our window
        win_start = 0
        # freq_Store will save the frequences of all our letters in s
        freq_store = {}

        # loop nth amount of times with n being the length of s
        for win_end in range(len(s)):
            # if the current char of s is in the freq_store:
              # add 1 to its freq, if not, add it to store and then add 1 to freq
            freq_store[s[win_end]] = 1 + freq_store.get(s[win_end], 0)
            # save the amount of the maximum frequency values in a variable max_freq
            max_freq = max(freq_store.values())

            # while the length of the window - the frequency of the maximum char is less than k:
             # this means we have way too many replacements.
            while ((win_end - win_start +1) - max_freq > k):
                # keep deleting from the freq_store until it is less than the length of the window - the frequency of the maximum char
                freq_store[s[win_start]] -= 1
                # update the start of our window since we are subtracting frequencies
                win_start += 1 
            # take the longest char to be the max between longest_char and the length of the window
            longest_char = max(longest_char, win_end - win_start +1)
        return longest_char
        

