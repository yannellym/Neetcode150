1143. Longest Common Subsequence
Solved
Medium
Topics
Companies
Hint
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
Seen this question in a real interview before?
1/4
Yes
No
Accepted
987.2K
Submissions
1.7M
Acceptance Rate
57.8%

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        
        
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # start at the bottom right of the grid
                
                if text2[j] == text1[i]:
                    # add the diagonal value to the coor in dp
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    # check the bottom and check the right, take the max between curr, bottom, right
                    dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j+1])
        # the res will be stored in the last coor visited as we have summed up to it. 
        return dp[0][0]

# https://www.youtube.com/watch?v=Ua0GhsJSlWM
