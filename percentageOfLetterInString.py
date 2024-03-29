# 2278. Percentage of Letter in String
# Easy
# 351
# 40
# Companies
# Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

 

# Example 1:

# Input: s = "foobar", letter = "o"
# Output: 33
# Explanation:
# The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.
# Example 2:

# Input: s = "jjjj", letter = "k"
# Output: 0
# Explanation:
# The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.
 

# Constraints:

# 1 <= s.length <= 100
# s consists of lowercase English letters.
# letter is a lowercase English letter.
# Accepted
# 46.1K
# Submissions
# 62.3K
# Acceptance Rate
# 74.0%

class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """

        return (s.count(letter)*100)//len(s)
