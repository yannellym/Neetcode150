984. String Without AAA or BBB
Solved
Medium
Topics
Companies
Given two integers a and b, return any string s such that:

s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
The substring 'aaa' does not occur in s, and
The substring 'bbb' does not occur in s.
 

Example 1:

Input: a = 1, b = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: a = 4, b = 1
Output: "aabaa"
 

Constraints:

0 <= a, b <= 100
It is guaranteed such an s exists for the given a and b.
Accepted
43.3K
Submissions
99.6K
Acceptance Rate
43.5% 

class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        result = ""  # Initialize an empty string to store the result.
    
        while a > 0 or b > 0:
            # Check which letter to add based on the remaining counts of 'a' and 'b'.
            if len(result) >= 2 and result[-1] == result[-2]:
                # If the last two characters are the same, add the other letter.
                if result[-1] == 'a':
                    result += "b"
                    b -= 1
                else:
                    result += "a"
                    a -= 1
            elif a > b:
                result += "a"  # Add "a" if there are more 'a's than 'b's.
                a -= 1
            else:
                result += "b"  # Add "b" if there are more 'b's than 'a's.
                b -= 1
        
        return result  # Return the final result string.
