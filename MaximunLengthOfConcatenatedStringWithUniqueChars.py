1239. Maximum Length of a Concatenated String with Unique Characters
Solved
Medium
Topics
Companies
Hint
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
Seen this question in a real interview before?
1/4
Yes
No
Accepted
187.5K
Submissions
359K
Acceptance Rate
52.2%
class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def canExtend(combination):
            return len(combination) == len(set(combination))

        maxi = 0 

        def findMax(start, path):
            nonlocal maxi
            for i in range(start, len(arr)):
                if canExtend(path + arr[i]):
                    maxi = max(maxi, len(path) + len(arr[i]))
                findMax(i+1, path + arr[i])
                

        findMax(0, "")
        return maxi

         
