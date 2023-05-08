# 1209. Remove All Adjacent Duplicates in String II
# Medium
# 5.1K
# 98
# Companies
# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

# Example 1:

# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
# Example 2:

# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"
# Example 3:

# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"
 

# Constraints:

# 1 <= s.length <= 105
# 2 <= k <= 104
# s only contains lowercase English letters.
# Accepted
# 264.7K
# Submissions
# 470.6K
# Acceptance Rate
# 56.3%

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []

        # for every char in s
        for char in s:
            # if the there is a stack and the num at top of stack equals our char
            if stack and stack[-1][0] == char:
                # add one to its count
                stack[-1][1] +=1
            else:
                # if not, add an arr of the char and 1 count thus far to the stack
                stack.append([char, 1])
            # if the count of the num at top of stack equals k, pop it from stack
            if stack[-1][1] == k:
                stack.pop()
        # join the chars in the stack by multiplying them by their count
        res = ""
        for char, count in stack:
            res += (char * count)
        return res

          
''' 
Example:           
[[u'd', 1]]
[[u'd', 1], [u'e', 1]]
[[u'd', 1], [u'e', 2]]
[[u'd', 1]]
[[u'd', 2]]
[[u'd', 2], [u'b', 1]]
[[u'd', 2], [u'b', 2]]
[[u'd', 2], [u'b', 2], [u'c', 1]]
[[u'd', 2], [u'b', 2], [u'c', 2]]
[[u'd', 2], [u'b', 2]]
[[u'd', 2]]
[]
[[u'a', 1]]
[[u'a', 2]]
'''
