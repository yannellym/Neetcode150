# 76. Minimum Window Substring
# Hard
# 14.8K
# 628
# Companies
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?

# Accepted
# 998.6K
# Submissions
# 2.4M
# Acceptance Rate
# 40.9%

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        from collections import Counter
        # create a dictionary that maps each character in `t` to its frequency
        char_freq = Counter(t)
        # initialize the left and right pointers, found counter, and minimum window variables
        left = 0
        right = 0
        found = 0
        min_window = ""
        min_len = float('inf')
        
        # loop until the `right` pointer reaches the end of the string `s`
        while right < len(s):
            # check if the current character at the `right` pointer is in `t`
            if s[right] in char_freq:
                # decrement the frequency of the character in the `char_freq` dictionary
                char_freq[s[right]] -= 1
                # if the frequency becomes zero or positive, increment the `found` counter
                if char_freq[s[right]] >= 0:
                    found += 1
            # once all characters in `t` have been found, start moving the `left` pointer
            while found == len(t):
                # if the current window is smaller than the minimum window found so far,
                # update the `min_window` and `min_len` variables
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right+1]
                # check if the current character at the `left` pointer is in `t`
                if s[left] in char_freq:
                    # increment the frequency of the character in the `char_freq` dictionary
                    char_freq[s[left]] += 1
                    # if the frequency becomes positive, decrement the `found` counter
                    if char_freq[s[left]] > 0:
                        found -= 1
                # move the `left` pointer to the right
                left += 1
            # move the `right` pointer to the right
            right += 1
        
        # return the minimum window substring
        return min_window

# alternative 

def StringChallenge(strArr):
    n_store = {}
    k_store = {}
    matches = {}

    N = strArr[0]
    K = strArr[1]

    res = []

    # sets up the dictionary for the K String
    for char in strArr[1]:
        k_store[char] = 1 + k_store.get(char, 0)

    # sliding window approach
    win_start = 0
    min_length = float('inf')

    for win_end in range(len(N)):
        # add the chars to the n_store
        n_store[N[win_end]] = 1 + n_store.get(N[win_end], 0)

        # if the char is also in k_store, let add it to our matches dic
        if N[win_end] in k_store:
            matches[N[win_end]] = 1 + matches.get(N[win_end], 0)

        # check if all characters in K are in the current window
        while all(k in matches and matches[k] >= k_store[k] for k in k_store):
            # calculate the current substring length
            curr_length = win_end - win_start + 1

            # if the current substring contains all characters in K and it's the smallest found so far,
            # update the result
