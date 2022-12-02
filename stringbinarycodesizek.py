# 1461. Check If a String Contains All Binary Codes of Size K
# Medium

# 1976

# 90

# Add to List

# Share
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
# 105,075
# Submissions
# 185,095

class Solution(object):
    def hasAllCodes(self, s, k):
        
        store = set()
        # goes through the length of s - k plus 1
        # this will ensure the loop leave 2 digits do count at the end
        # it will also add 1 to make sure it is inclusive
        for i in range(len(s)-k + 1): 
            # it will add to the store the values from i to i + k
            store.add(s[i: i + k])
        # for this instance, k = 2
        # if there are 4 unique strings in the set
        # this means that all substrings are there
        # since its 1 and 0s, you can make a combination of 4 diff strings 
        # 2 ^2 = 2 x 2
        # if k were 3, you could make 8 diff combinations
        # 2 ^3 = 2 x 2 x 2
        return len(store) == 2**k 
    
