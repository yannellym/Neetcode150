# 1704. Determine if String Halves Are Alike
# Easy
# 1.6K
# 79
# Companies
# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.

 

# Example 1:

# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
# Example 2:

# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
# Notice that the vowel o is counted twice.
 

# Constraints:

# 2 <= s.length <= 1000
# s.length is even.
# s consists of uppercase and lowercase letters.
# Accepted
# 184.7K
# Submissions
# 237.4K
# Acceptance Rate
# 77.8%


class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bank = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
      
      # first approach
        # mid = len(s)//2
        # left, right = s[:mid], s[mid:]
        # storeL = 0
        # storeR = 0

        # for i in range(len(left)):
        #     if left[i] in bank:
        #         storeL +=1
        #     if right[i] in bank:
        #         storeR +=1
        # return storeL == storeR
        
     # second approach
        i = 0
        j = len(s)-1
        countL = 0
        countR = 0

        while i<j:
            if s[i] in bank:
                countL +=1
            if s[j] in bank:
                countR +=1
            i +=1
            j-=1
        return countL == countR
# third approach

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        n = len(s)
        l = 0
        r = 0

        for i in range(n//2):
            if s[i] in vowels:
                l +=1
            if s[(n//2)+i] in vowels:
                r +=1
        return l == r

