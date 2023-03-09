# 1324. Print Words Vertically
# Medium
# 635
# 106
# Companies
# Given a string s. Return all the words vertically in the same order in which they appear in s.
# Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
# Each word would be put on only one column and that in one column there will be only one word.

 

# Example 1:

# Input: s = "HOW ARE YOU"
# Output: ["HAY","ORO","WEU"]
# Explanation: Each word is printed vertically. 
#  "HAY"
#  "ORO"
#  "WEU"
# Example 2:

# Input: s = "TO BE OR NOT TO BE"
# Output: ["TBONTB","OEROOE","   T"]
# Explanation: Trailing spaces is not allowed. 
# "TBONTB"
# "OEROOE"
# "   T"
# Example 3:

# Input: s = "CONTEST IS COMING"
# Output: ["CIC","OSO","N M","T I","E N","S G","T"]
 

# Constraints:

# 1 <= s.length <= 200
# s contains only upper case English letters.
# It's guaranteed that there is only one space between 2 words.
# Accepted
# 32.8K
# Submissions
# 53.4K
# Acceptance Rate
# 61.4%

class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # split the sentence into words
        s = s.split(" ")
        # get the max word from s and filter by length
        maxi = max(s, key = len)
        # res array to keep track of our values added
        res = []

        # iterate the length of maxi
        for i in range(len(maxi)):
            # this is the string that will be added to res
            level = ""
            # for every word in s
            for word in s:
                # if the index is less than the length of the word (within range)
                if i < len(word):
                    # add the letter to the level
                    level+= word[i]
                else:
                    # else, add a space to the level
                    level += " "
            # append the level to the res
            res.append(level)
        # return each level in res and strip the last spaces
        return [s.rstrip() for s in res]



