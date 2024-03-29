https://leetcode.com/problems/license-key-formatting/description/


482. License Key Formatting
Solved
Easy
Topics
Companies
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

 

Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:

Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
 

Constraints:

1 <= s.length <= 105
s consists of English letters, digits, and dashes '-'.
1 <= k <= 104
Seen this question in a real interview before?
1/4
Yes
No
Accepted
273.4K
Submissions
626.7K
Acceptance

Rate
43.6%

class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Remove dashes and convert lowercase letters to uppercase
        s = s.replace("-", "").upper()
        
        # Reverse the string for easier grouping
        s = s[::-1]
        for i in range(0, len(s), k):
            print(i)
            print(s[i:i+k]) 
        # Group characters into groups of length k
        groups = [s[i:i+k] for i in range(0, len(s), k)]
        
        # Join the groups with dashes
        result = "-".join(groups)
        
        # Reverse the result to obtain the final output
        return result[::-1]
