2405. Optimal Partition of String
Solved
Medium
Topics
Companies
Hint
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

 

Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
 

Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.
Accepted
134.5K
Submissions
169.9K
Acceptance Rate
79.1%

class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        substr_count = 0

        for char in s:
            if char in seen:
                substr_count += 1
                seen.clear()
            seen.add(char)

        # Add the last substring if there are any characters left
        if seen:
            substr_count += 1

        return substr_count
