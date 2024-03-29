# 13. Roman to Integer
# Easy

# 6803

# 410

# Add to List

# Share
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].


class Solution(object):
    def romanToInt(self, s):
        
        store = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        
        sum = 0
        for i in s:
            sum += store[i]
        return sum
       
# better solution
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # store to reference the values of the keys
        store = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L': 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        count = 0
        # iterate the length of s
        for i in range(len(s)):
            # if we're within bounds while referring to i+1
            # AND the value of s[i] in the store is less than the value of s[i+1] in the store
            if i + 1 < len(s) and store[s[i]] < store[s[i+1]]:
                # subtract from that value from the count as s[i] is less than s[i+1]
                count -= store[s[i]]
            else:
                # else, add it
                count += store[s[i]]
        return count

        # ex, CMXCVIII
        '''
        C < M  COUNT = 100
        M > X  COUNT  = +1000   = 900
        X < C  COUNT = -10   = 890
        C > V  COUNT = + 100 = 990
        V > I  COUNT = + 5  = 995
        ....III. COUNT = 998
        '''
