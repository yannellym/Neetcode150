159. Longest Substring with At Most Two Distinct Characters
Solved
Medium
Topics
Companies
Given a string s, return the length of the longest 
substring
 that contains at most two distinct characters.

 

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
 

Constraints:

1 <= s.length <= 105
s consists of English letters.
Seen this question in a real interview before?
1/4
Yes
No
Accepted
242.7K
Submissions
444.8K
Acceptance Rate
54.6%

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        store = {}

        win_s = 0
        long_sub = 0
        for win_e in range(len(s)):
            store[s[win_e]] = 1 + store.get(s[win_e], 0)        
         
            if len(store.keys()) > 2:
          
                store[s[win_s]] -=1 
                if store[s[win_s]] == 0:
                    del store[s[win_s]]
             
                win_s +=1
 
            long_sub = max(long_sub, win_e+1 - win_s)
     
        return long_sub
