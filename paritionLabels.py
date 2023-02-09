# 763. Partition Labels
# Medium
# 9.1K
# 341
# Companies
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

 

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.
# Accepted
# 450.8K
# Submissions
# 565K
# Acceptance Rate
# 79.8%


class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # create a dict to save the values and their last index
        store = {}
        # enumerate s to get each char and index
        for index, char in enumerate(s):
            # update each char to its index
            # this will will update each char to its last index at the end
            store[char] = index
        # keeps track of our response
        res = []
        # the length of the string
        length = 0
        # keeps track of the last major index of chars we have seen
        end = 0
        # enumerate s to get each char and index
        for index, char in enumerate(s):
            # increment the length since we are looking at anothe char
            length += 1
            # see to see which is greater, our current end or this char' last index in the store
            # this will give our the new ending of our partition
            end = max(end, store[char])
            # if the index equals the end, however,
            if index == end:
                # append the length to the res 
                res.append(length)
                # set the length now to 0
                length = 0
                # we dont need to update the index because it will update automatically once
                # it keeps going to the right
        # return the arr of lengths
        return res
