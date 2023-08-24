# 767. Reorganize String
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.
# Accepted
# 329K
# Submissions
# 606.2K
# Acceptance Rate
# 54.3%

import heapq
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Count the frequency of each character in the string
        char_count = Counter(s)
        
        # Create a max heap of characters based on their frequencies
        max_heap = [(-count, char) for char, count in char_count.items()]
        heapq.heapify(max_heap)
        
        result = []
        
        while len(max_heap) >= 2:
            # Get the two most frequent characters
            neg_count1, char1 = heapq.heappop(max_heap)
            neg_count2, char2 = heapq.heappop(max_heap)
            
            # Add the characters to the result alternately
            result.extend([char1, char2])
            
            # Decrease the frequencies and add back to heap if necessary
            # the count of the number can't be negative. so itll be: 8 -> heap[-8]
            # if it ever gets to 0, it means that all of its values were used. 
            if neg_count1 + 1 != 0:
                heapq.heappush(max_heap, (neg_count1 + 1, char1))
            if neg_count2 + 1 != 0:
                heapq.heappush(max_heap, (neg_count2 + 1, char2))
        
        # If there's one character remaining in the heap
        if max_heap:
            neg_count, char = heapq.heappop(max_heap)
            if neg_count < -1:
                return ""  # Not possible to reorganize
            
            result.append(char)
        
        return "".join(result)
