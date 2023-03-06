# 2399. Check Distances Between Same Letters
# Easy
# 327
# 26
# Companies
# You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly twice. You are also given a 0-indexed integer array distance of length 26.

# Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).

# In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i]. If the ith letter does not appear in s, then distance[i] can be ignored.

# Return true if s is a well-spaced string, otherwise return false.

 

# Example 1:

# Input: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: true
# Explanation:
# - 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
# - 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
# - 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
# Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
# Return true because s is a well-spaced string.
# Example 2:

# Input: s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: false
# Explanation:
# - 'a' appears at indices 0 and 1 so there are zero letters between them.
# Because distance[0] = 1, s is not a well-spaced string.
 

# Constraints:

# 2 <= s.length <= 52
# s consists only of lowercase English letters.
# Each letter appears in s exactly twice.
# distance.length == 26
# 0 <= distance[i] <= 50
# Accepted
# 33.5K
# Submissions
# 47.5K
# Acceptance Rate
# 70.6%


class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        # a map to keep our indices
        store = defaultdict(int) 

        # enumerate s
        for i, c in enumerate(s):
            # if the char is not in the store
            if c not in store:
                # add the char to the store along with its index
                store[c] = i
            else:
                # if it is already in the store, take i and subtract the value of the char in store - 1
                store[c] = i - store.get(c) - 1
        
        # store = {u'a': 1, u'c': 0, u'b': 3}
        
        # for all keys, and values in store      
        for k, v in store.items():
            # if the distance of the ord value of k minus 97 doesnt equal the value of v, return 
            # ord('a') is 97. So 97-97 = 0
            # dkistance[0] = 1    1 == v(1)
            if distance[ord(k) - 97] != v:
                return False
        return True 
            
