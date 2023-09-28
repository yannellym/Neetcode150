880. Decoded String at Index
Solved
Medium
Topics
Companies
You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.

 

Example 1:

Input: s = "leet2code3", k = 10
Output: "o"
Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: s = "ha22", k = 5
Output: "h"
Explanation: The decoded string is "hahahaha".
The 5th letter is "h".
Example 3:

Input: s = "a2345678999999999999999", k = 1
Output: "a"
Explanation: The decoded string is "a" repeated 8301530446056247680 times.
The 1st letter is "a".
 

Constraints:

2 <= s.length <= 100
s consists of lowercase English letters and digits 2 through 9.
s starts with a letter.
1 <= k <= 109
It is guaranteed that k is less than or equal to the length of the decoded string.
The decoded string is guaranteed to have less than 263 letters.
Accepted
83.8K
Submissions
230.7K
Acceptance Rate
36.4%


class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        decoded_length = 0  # Initialize the decoded length to 0

        # Calculate the decoded length without actually decoding the string
        for char in s:
            if char.isalpha():  # If it's an alphabet character
                decoded_length += 1
            else:  # If it's a digit character
                decoded_length *= int(char)
        '''
        Example:
            s = "leet2code3"
            k = 10
            decoded_length = 36
        '''
        # Work backward to find the kth character
        # ['3', 'e', 'd', 'o', 'c', '2', 't', 'e', 'e', 'l']
        for char in reversed(s):
            k %= decoded_length  # Update k based on the decoded length
            if k == 0 and char.isalpha():  # If k becomes 0 and we encounter an alphabet character
                return char
            if char.isalpha():  # If it's an alphabet character
                decoded_length -= 1
            else:  # If it's a digit character
                decoded_length /= int(char)  # Divide the decoded length by the digit value
