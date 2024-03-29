# 17. Letter Combinations of a Phone Number
# Medium
# 14.3K
# 823
# Companies
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
# Accepted
# 1.5M
# Submissions
# 2.7M
# Acceptance Rate
# 56.4%

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        # if the digits is empty "" return an empty array
        if digits == "":
            return []

        # map the number to values
        store = { 
            '1': "",
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"],
        }
        # helper recursive func
        def backtrack(i, curStr):
            # if the length of the string equals the length of digits,
            # append it to the res and return 
            if len(curStr) == len(digits):
                res.append(curStr)
                return
                # this will perform the backtracking 
            # for char in the selected ith char of digits in store
            for c in store[digits[i]]:
                # call the backtrack func on the ith plus 1,
                # and the curr string plus the char
                backtrack(i+1, curStr + c)
        
        res = []
        backtrack(0, "")
        return res

       # the idea is to take each number in digits and backtrack the letters on the rest of the numbers in digits.
       # this will create combintations that are the same length as digits.
       # if the string that we're creating ever gets to be the same length as digits, we append it to the res and then return.
       # for every value in store[digits[value]], we call backtrack and increase the digit by one and add the value to the curr str
       
       
        '''
        i	0
        curStr	""
        c	"a"


        backtrack [parent=f1]
        i	1
        curStr	"a"
        c	"d"


        backtrack [parent=f1]
        i	2
        curStr	"ad"

        backtrack [parent=f1]
        i	2
        curStr	"ad"
        Return
        value	None # here the string equals the same length as digits so it adds it to res and returns


        backtrack [parent=f1] # now moves to second value in digits[1]
        i	1
        curStr	"a"
        c	"e"


        '''
