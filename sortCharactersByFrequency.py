# 451. Sort Characters By Frequency
# Medium
# 6.4K
# 226
# Companies
# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

 

# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
 

# Constraints:

# 1 <= s.length <= 5 * 105
# s consists of uppercase and lowercase English letters and digits.
# Accepted
# 490.1K
# Submissions
# 699.9K
# Acceptance Rate
# 70.0%

class Solution:
    def frequencySort(self, s: str) -> str:

        # First, put s in a set
        # Second, list comprehension: 
          # for every x in the set, multiply x by its count in S
        # Third, sort it by its length
        # Fourth, reversed it, you want the greater values at the beginning
        # Fifth, join the string and return it
        res = sorted([x * s.count(x) for x in set(s)], key=len, reverse=True)
        return ''.join(res)

        # Edge case addressed:

            # loveleetcode
            # Counter({'e': 4, 'l': 2, 'o': 2, 'v': 1, 't': 1, 'c': 1, 'd': 1})
