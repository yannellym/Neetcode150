# 409. Longest Palindrome
# Easy
# 4.2K
# 252
# Companies
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.
# Accepted
# 445.7K
# Submissions
# 817.5K
# Acceptance Rate
# 54.5%



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if there's just one letter in the input, return 1
        if len(s) == 1:
            return 1
        # store all values in a map
        store = {}
        for letter in s:
            store[letter] = 1 + store.get(letter, 0)
        # set variables to count the odd and even values
        res = 0
        odd = 0
        # go through each value count in the store
        for value in store.values():
            # if the value is 1, add it to the odd count and continue
            if value == 1:
                odd += 1
                continue
            # if the value is divisible by 2, add that value to the res
            if value % 2 == 0:
                res += value
            else:
                # else take that value and subract one ( to make it even) 
                # and add the remaining (1) to the odd variable
                res += value - 1
                odd += 1
        # return res + ( 1 if you the odd variable is > 0, which means we have left over counts)
        # with this left over count, we can make words such as "ccddfddcc". They go in the middle
        # else, you add 0 because we don't have any leftovers
        return res + (1 if odd else 0)
