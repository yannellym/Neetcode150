# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.

 

# Example 1:

# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:

# Input: s = "3z4"
# Output: ["3z4","3Z4"]
 

# Constraints:

# 1 <= s.length <= 12
# s consists of lowercase English letters, uppercase English letters, and digits.
# Accepted
# 261.7K
# Submissions
# 355K
# Acceptance Rate
# 73.7%

class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # stores our array of permutations
        output = [""]
        # for every instance in our string
        for c in s:
            # create a temp array
            tmp = []
            # if the instance is a letter
            if c.isalpha():
                # for every char in the output
                for o in output:
                    # to the temp, append the char plus the instance lowercase
                    tmp.append(o+c.lower())
                    # to the temp, append the char plus the instance lowercase
                    tmp.append(o+c.upper())
            else:
                # else, for every char in the output
                for o in output:
                    # append to the temp, the output and the char
                    tmp.append(o+c)
            # have the output equal the temp
            output = tmp
        return output
    
