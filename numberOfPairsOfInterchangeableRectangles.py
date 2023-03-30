# 2001. Number of Pairs of Interchangeable Rectangles
# Medium
# 370
# 33
# Companies
# You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.

# Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).

# Return the number of pairs of interchangeable rectangles in rectangles.

 

# Example 1:

# Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]
# Output: 6
# Explanation: The following are the interchangeable pairs of rectangles by index (0-indexed):
# - Rectangle 0 with rectangle 1: 4/8 == 3/6.
# - Rectangle 0 with rectangle 2: 4/8 == 10/20.
# - Rectangle 0 with rectangle 3: 4/8 == 15/30.
# - Rectangle 1 with rectangle 2: 3/6 == 10/20.
# - Rectangle 1 with rectangle 3: 3/6 == 15/30.
# - Rectangle 2 with rectangle 3: 10/20 == 15/30.
# Example 2:

# Input: rectangles = [[4,5],[7,8]]
# Output: 0
# Explanation: There are no interchangeable pairs of rectangles.
 

# Constraints:

# n == rectangles.length
# 1 <= n <= 105
# rectangles[i].length == 2
# 1 <= widthi, heighti <= 105
# Accepted
# 24K
# Submissions
# 52.2K
# Acceptance Rate
# 46.1%


import decimal

class Solution(object):
    def interchangeableRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        count = 0
        store = {}
        
        # go through each rectangle in rectangles
        for i in range(len(rectangles)):
            curr = rectangles[i]
            # add their decimal division to the store. Add 1 each time it repeats
            store[decimal.Decimal(curr[0])/decimal.Decimal(curr[1])] = 1 + store.get(decimal.Decimal(curr[0])/decimal.Decimal(curr[1]), 0)
        
        # for every value in store.values
        for value in store.values():
            # if the value is greater than one (because you need more than 1 for a pair)
            if value > 1:
                # to the count, add the value -1 * the value then floor division by 2
                # WHY: Ex. value = 4  there are only 3 other values we can look at. So we need to do 4-1 (factorial)
                # then, multitply that original value by its factorial. Finally, that would give us the permutation. 
                # meaning that it has a lot of duplicates. We only need the original values so we divide by 2.
                count += ((value - 1) * value )// 2
        return count
