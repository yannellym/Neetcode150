# 1461. Check If a String Contains All Binary Codes of Size K
# Medium
# 2.1K
# 90
# Companies
# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 

# Example 1:

# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
# Example 2:

# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
# Example 3:

# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and does not exist in the array.
 

# Constraints:

# 1 <= s.length <= 5 * 105
# s[i] is either '0' or '1'.
# 1 <= k <= 20
# Accepted
# 108.9K
# Submissions
# 192.3K
# Acceptance Rate
56.6%

class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # a set for our combinations
        store = set()

        # we are going to iterate through the string and check every sub string
        # -k here to make sure we have k numbers to compare at the end
        # + 1 to make sure we stay within bounds
        for i in range(len(s)-k+1):
            # add it to the store, it will only be original ones added
            store.add(s[i:i+k])
        # if the len of the store(how many unique substrings of len k we have) equals k ** 2 return true
        # k ** 2 because for every number we have 2 cobinations of binary. ex,    _ (a 1 or 0)  _ (a 1 or 0)
        # we multiply two by whatever number k is 
        return len(store) == 2 **k 
