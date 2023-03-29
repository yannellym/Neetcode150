# 1930. Unique Length-3 Palindromic Subsequences
# Medium
# 648
# 19
# Companies
# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

# A palindrome is a string that reads the same forwards and backwards.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
 

# Example 1:

# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")
# Example 2:

# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".
# Example 3:

# Input: s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")


# Constraints:

# 3 <= s.length <= 105
# s consists of only lowercase English letters.
# Accepted
# 23.2K
# Submissions
# 44.6K
# Acceptance Rate
# 52.0%
 

  
  class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """

        # approach:
        '''
        1. iterate through s and get the index and the char
        2. for each char that is not in the store,add the char to the store with the beginning index and the last index
        3. if its in the store, update the last char index with the new index of this char
        4. iterate through store.items and get the char and they values
        5. to the res, add the length of the set of the slice of s from start idx +1 to end idx
        6. return the res
        '''
        store = {}
        # iterate through each char in s and get the index and the char
        for i, c in enumerate(s):
            # if the char is not in the store
            if c not in store:
                # if it is not already in d, a new key-value pair is added to store
                # with the character as the key and a list of two indices as the value. 
                # The two indices represent the starting and ending indices of the 
                # substring containing the character. 
                store[c] = [i, i]
            else:
                # if in the store, the ending index of the substring is updated to 
                # the current index i.
                store[c][1] = i
    
        res = 0
        for c, (start_idx, end_idx) in store.items():
            
            res += len(set(s[start_idx + 1:end_idx]))
        return res

        # store {u'a': [0, 4], u'c': [3, 3], u'b': [2, 2]}

        # So, len(set(s[start_idx + 1:end_idx])) essentially calculates the number of unique 
        # characters in the substring that contains a particular character c, excluding the first 
        # character of the substring. This value is then added to the running total res, which keeps track 
        # of the count of all unique substrings of length greater than one in the string.
