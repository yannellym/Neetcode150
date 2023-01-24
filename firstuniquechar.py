# 387. First Unique Character in a String
# Easy
# 7.3K
# 248
# Companies
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.
# Accepted
# 1.3M
# Submissions
# 2.2M
# Acceptance Rate
# 59.3%

#from collections import OrderedDict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # look at each char in s
        for char in s:
            # if the current char's index equals the current's char last occurence's index
            if s.index(char) == s.rindex(char):
                # return the index of the char
                # this means that there's only one of them
                return s.index(char)
        # if there's no char that only repeats once, return -1
        return -1



        # create an ordered dict to keep an ordered representation of our values
        # store = OrderedDict()
        # loop through s
        # for i in range(len(s)):
        #     # add the char to the store, if not there
                # add it to the char if there 
        #     store[s[i]] = 1 + store.get(s[i], 0)
    
        # for every key, and every values in the store's items
        # for key, value in store.items():
        #   # if the value of the key equals one
        #     if value == 1:
                    # return the index of that key
                    # this works because our dict is ordered so itll git the first
                    # key with a value of 1 and return 
        #         return s.index(key)
        # if no key has a 1 value, it'll return -1
        # return -1
