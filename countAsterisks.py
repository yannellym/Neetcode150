# 2315. Count Asterisks
# Easy
# 412
# 63
# Companies
# You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

# Return the number of '*' in s, excluding the '*' between each pair of '|'.

# Note that each '|' will belong to exactly one pair.

 

# Example 1:

# Input: s = "l|*e*et|c**o|*de|"
# Output: 2
# Explanation: The considered characters are underlined: "l|*e*et|c**o|*de|".
# The characters between the first and second '|' are excluded from the answer.
# Also, the characters between the third and fourth '|' are excluded from the answer.
# There are 2 asterisks considered. Therefore, we return 2.
# Example 2:

# Input: s = "iamprogrammer"
# Output: 0
# Explanation: In this example, there are no asterisks in s. Therefore, we return 0.
# Example 3:

# Input: s = "yo|uar|e**|b|e***au|tifu|l"
# Output: 5
# Explanation: The considered characters are underlined: "yo|uar|e**|b|e***au|tifu|l". There are 5 asterisks considered. Therefore, we return 5.
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters, vertical bars '|', and asterisks '*'.
# s contains an even number of vertical bars '|'.
# Accepted
# 41.4K
# Submissions
# 50.3K
# Acceptance Rate
# 82.2%

class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        # split the word where there are "|"s
        splitted = s.split('|')
        print(splitted)
        # create a var with 0
        c = 0
        # enumerate splitted
        # for index, and string in enumerated splitted
        for i, string in enumerate(splitted):
            # if the index modulo 2 is 0 (idex is either 0, 2, 4..) then we count how many asteriks they have
            # since the |s came in pairs, every odd index is going to be one that was outside of each pair
            if i % 2 == 0:
                # add the count of that string to c
                c += string.count('*')
        return c
