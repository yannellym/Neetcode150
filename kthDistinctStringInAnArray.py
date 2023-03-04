# 2053. Kth Distinct String in an Array
# Easy
# 570
# 19
# Companies
# A distinct string is a string that is present only once in an array.

# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

# Note that the strings are considered in the order in which they appear in the array.

 

# Example 1:

# Input: arr = ["d","b","c","b","c","a"], k = 2
# Output: "a"
# Explanation:
# The only distinct strings in arr are "d" and "a".
# "d" appears 1st, so it is the 1st distinct string.
# "a" appears 2nd, so it is the 2nd distinct string.
# Since k == 2, "a" is returned. 
# Example 2:

# Input: arr = ["aaa","aa","a"], k = 1
# Output: "aaa"
# Explanation:
# All strings in arr are distinct, so the 1st string "aaa" is returned.
# Example 3:

# Input: arr = ["a","b","a"], k = 3
# Output: ""
# Explanation:
# The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
 

# Constraints:

# 1 <= k <= arr.length <= 1000
# 1 <= arr[i].length <= 5


# arr[i] consists of lowercase English letters.
# Accepted
# 41.4K
# Submissions
# 57.5K
# Acceptance Rate
# 72.0%

from collections import OrderedDict

class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """

        store = OrderedDict()
        res = []
        for char in arr:
            if char in store:
                store[char] +=1
            else:
                store[char] = 0
        for key, v in store.items():
            if v == 0:
                res.append(key)
        return res[k-1] if len(res) >= k else ""
