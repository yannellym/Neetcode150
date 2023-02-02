# 1046. Last Stone Weight
# Easy
# 4.1K
# 79
# Companies
# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

 

# Example 1:

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
# Example 2:

# Input: stones = [1]
# Output: 1
 

# Constraints:

# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
# Accepted
# 377.9K
# Submissions
# 583.2K
# Acceptance Rate
# 64.8%

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # python doesnt have a max heap, just a min heap.
        # due to this, we have to implement a min heap with negative values
        stones = [-x for x in stones]
        # make the list into a heap
        # this will arrange values from smallest to largest and always pop the next min element
        heapq.heapify(stones)

        # while the length of stones is greater than 1
         # this will make sure we can always pop 2 elements
        while len(stones) >1:
            # get the first and second max elements
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            # if b element is greater and not equal to a 
              # (which it should be because they are negatives)
            if b > a:
                # subtract: a- b . Ex -8 - -7 = -1
                c = a-b
                # push the result in the heap
                heapq.heappush(stones,c)
        # this would take care of the case that the heap doesnt have any elements inside:
         # insert a 0 to the list in case we have no elements left in the heap
        stones.append(0)
        # return the absolute values of the first element in the heap(values were negative)
        return abs(stones[0])
