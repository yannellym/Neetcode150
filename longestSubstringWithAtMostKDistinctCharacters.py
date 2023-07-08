# 340. Longest Substring with At Most K Distinct Characters
# Medium
# 2.7K
# 77
# company
# Yandex
# company
# Amazon
# company
# Google
# Given a string s and an integer k, return the length of the longest 
# substring
#  of s that contains at most k distinct characters.

 

# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
# Example 2:

# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.
 

# Constraints:

# 1 <= s.length <= 5 * 104
# 0 <= k <= 50
# Accepted
# 314.6K
# Submissions
# 654.2K
# Acceptance Rate
# 48.1%

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        win_s = 0
        store = {}
        longest = 0

        # for every char in s
        for win_e in range(len(s)):
            # add it to the store if its not there, and then add 1
            # if its there, just add 1
            store[s[win_e]] = 1 + store.get(s[win_e], 0)
            # get the size of the store, that will tell us how many diff keys there are 
            num_k = len(store.keys())

            # if the size of the store is greater than k, that means we have too many letters
            if num_k > k:
                # in the store, find the value of the char from s at index win_s and subtract 1 from it
                store[s[win_s]] -=1 
                # if the value is 0, we want to remove it so it doesnt count as a key
                if store[s[win_s]] == 0:
                    del store[s[win_s]]
                # increase the win_s index so we make the window smaller
                win_s +=1
            # make longest equal the longest between longest or the window size.
            longest = max(longest, win_e - win_s +1)
        return longest
