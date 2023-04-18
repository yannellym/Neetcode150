# 1888. Minimum Number of Flips to Make the Binary String Alternating
# Medium
# 964
# 36
# Companies
# You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

# Type-1: Remove the character at the start of the string s and append it to the end of the string.
# Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
# Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

# The string is called alternating if no two adjacent characters are equal.

# For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 

# Example 1:

# Input: s = "111000"
# Output: 2
# Explanation: Use the first operation two times to make s = "100011".
# Then, use the second operation on the third and sixth elements to make s = "101010".
# Example 2:

# Input: s = "010"
# Output: 0
# Explanation: The string is already alternating.
# Example 3:

# Input: s = "1110"
# Output: 1
# Explanation: Use the second operation on the second element to make s = "1010".
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '0' or '1'.
# Accepted
# 18.4K
# Submissions
# 47.3K
# Acceptance Rate
# 38.8%
class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        # the length of s
        n = len(s)
        # s will now equal double its sized
        s = s + s
        alt1 = ""
        alt2 = ""
        # make two strings that alternate for ith iterations
        for i in range(len(s)):
            alt1 += "0" if i % 2 else "1"
            alt2 += "1" if i % 2 else "0"
        
        res = len(s)
        diff1, diff2 = 0, 0
        
        # we'll start a sliding window
        win_start = 0
        '''
        s =    '111000111000'
        alt1 = '101010101010'
        alt2 = '010101010101'
        '''
        print(alt1, alt2)
        for win_end in range(len(s)):
            # if they're not the same, add to the diff 
            if s[win_end] != alt1[win_end]:
                diff1 +=1
            # if they're not the same, add to the diff 
            if s[win_end] != alt2[win_end]:
                diff2 +=1
            # if its a window bigger than what we need it to be
            if (win_end - win_start +1) > n:
                # subtract 1 to the diff if they're not the same 
                if s[win_start] != alt1[win_start]:
                    diff1 -=1 
                # subtract 1 to the diff if they're not the same 
                if s[win_start] != alt2[win_start]:
                    diff2 -=1 
                # shorten the window by incrementing win_start
                win_start +=1
            # if the window length is of length n(our right size), lets take the min res
            if (win_end - win_start +1) == n:
                res = min(res, diff1, diff2)
        return res

    '''
    step 1:
        get the original length
        double s's length
        alternate the strings and store them in new ones
    Step 2: 
        make res the length of s
        declare two diff variables
    Step 3:
        set up a sliding window
        if they're not the same subtract to the diff 
        if the window is bigger than n, 
        check if theres a diff again between the window start
        increase the window start
    Step 4: 
        check if the window length is n(our correct size). and set the res to the min

    '''
