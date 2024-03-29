# 692. Top K Frequent Words
# Medium
# 6.6K
# 311
# Companies
# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

# Example 1:

# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:

# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

# Constraints:

# 1 <= words.length <= 500
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# k is in the range [1, The number of unique words[i]]
 

# Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?

# Accepted
# 518.5K
# Submissions
# 910K
# Acceptance Rate


from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = Counter(words)
        ans = sorted(counts, key = lambda x: (-counts[x], x))
        return ans[:k]

        # Here lambda x:(-d[x],x) is a comparator, so first it will check the count of key(x) 
        # in the dictionary and -ve sign tells that sort in decreasing order of number of occurrence 
        # of a value

        # The 2nd arg in lambda x:(-d[x],x) is x tells if occurrence of two elements is 
        # same then place lesser value first and that's why you're seeing 2 before 5.
