https://leetcode.com/problems/palindrome-partitioning/



Code

Testcase
Testcase
Result

131. Palindrome Partitioning
Solved
Medium
Topics
Companies
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
Accepted
702.9K
Submissions
1.1M
Acceptance Rate
66.2%

def partition_palindromes(s):
    # Helper function to check if a string is a palindrome
    def is_palindrome(string):
        return string == string[::-1]

    # Backtracking function to generate palindrome partitions
    def backtrack(start, path):
        # If we have reached the end of the string, add the current partition to the result
        if start == len(s):
            result.append(path[:])
            return

        # Explore all possible substrings starting from the current position
        for end in range(start + 1, len(s) + 1):
            # Check if the current substring is a palindrome
            if is_palindrome(s[start:end]):
                # If it is a palindrome, add it to the current partition and continue exploring
                path.append(s[start:end])
                backtrack(end, path)
                # Remove the last added substring to backtrack and explore other possibilities

                path.pop()  # Backtrack by removing the last added substring

    result = []  # List to store all palindrome partitions
    backtrack(0, [])  # Start the backtracking process from the beginning
    return result

# Example usage:
s1 = "aab"
print(partition_palindromes(s1))  # Output: [["a", "a", "b"], ["aa", "b"]]

s2 = "a"
print(partition_palindromes(s2))  # Output: [["a"]]

