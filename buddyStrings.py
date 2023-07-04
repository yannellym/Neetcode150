# https://leetcode.com/problems/buddy-strings/description/

# 859. Buddy Strings
# Easy
# 2.8K
# 1.6K
# company
# DoorDash
# company
# Square
# company
# Facebook
# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

# Example 1:

# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
# Example 2:

# Input: s = "ab", goal = "ab"
# Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
# Example 3:

# Input: s = "aa", goal = "aa"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
 

# Constraints:

# 1 <= s.length, goal.length <= 2 * 104
# s and goal consist of lowercase letters.
# Accepted
# 204K
# Submissions
# 621.7K
# Acceptance Rate
# 32.8%

class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False  # If lengths are not equal, we can't make the strings equal by swapping letters
    
        if s == goal:
            # Check for at least two identical characters in the same string
            seen = set()
            for char in s:
                if char in seen:
                    return True  # If we find at least two identical characters, we can swap them to obtain goal
                seen.add(char)
            
            return False  # No two identical characters found, so we can't make the strings equal by swapping letters
        
        diffs = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diffs.append((s[i], goal[i]))  # Collect differing characters between s and goal
                if len(diffs) > 2:
                    return False  # If there are more than two differences, we can't make the strings equal by swapping letters
        print(diffs)
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]  
        # If there are exactly two differences, check if swapping them makes the strings equal
                    
