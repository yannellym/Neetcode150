459. Repeated Substring Pattern
Solved
Easy
Topics
Companies
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
Accepted
387.7K
Submissions
842K
Acceptance Rate
46.0%
Seen this question in a real interview before?
1/4

 n = len(s)
    
    # Iterate through possible substring lengths
    for i in range(1, n // 2 + 1):
        if n % i == 0:  # Check if the length of s is divisible by the current substring length
            substring = s[:i]  # Extract the current substring
            num_repeats = n // i  # Calculate the number of times the substring should be repeated
            constructed_string = substring * num_repeats  # Construct a string using the repeated substring
            
            if constructed_string == s:  # Compare the constructed string with the original string
                return True  # If they match, the string can be constructed using a repeated substring
    
    return False  # If no valid substring is found, return False
