# 1523. Count Odd Numbers in an Interval Range
# Easy
# 2.3K
# 137
# Companies
# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

# Example 1:

# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].
# Example 2:

# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].
 

# Constraints:

# 0 <= low <= high <= 10^9
# Accepted
# 260.2K
# Submissions
# 522.6K
# Acceptance Rate
# 49.8%

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # get the length of the number range 
         # plus 1 so we make sure we inlude the last one
        length = high - low + 1
        # floor division of length 
        # this makes sure its not a float
        count =  length // 2 
        # if the length is odd ( % 2 == 1) and low is odd
        if length % 2 == 1 and low % 2 == 1:
            # add 1 to the count since we're missing one more value
            count += 1
        #return the count
        return count


        
