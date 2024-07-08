# 1823. Find the Winner of the Circular Game
# Medium
# 2.2K
# 44
# Companies
# There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

# The rules of the game are as follows:

# Start at the 1st friend.
# Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
# The last friend you counted leaves the circle and loses the game.
# If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
# Else, the last friend in the circle wins the game.
# Given the number of friends, n, and an integer k, return the winner of the game.

 

# Example 1:


# Input: n = 5, k = 2
# Output: 3
# Explanation: Here are the steps of the game:
# 1) Start at friend 1.
# 2) Count 2 friends clockwise, which are friends 1 and 2.
# 3) Friend 2 leaves the circle. Next start is friend 3.
# 4) Count 2 friends clockwise, which are friends 3 and 4.
# 5) Friend 4 leaves the circle. Next start is friend 5.
# 6) Count 2 friends clockwise, which are friends 5 and 1.
# 7) Friend 1 leaves the circle. Next start is friend 3.
# 8) Count 2 friends clockwise, which are friends 3 and 5.
# 9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.
# Example 2:

# Input: n = 6, k = 5
# Output: 1
# Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.
 

# Constraints:

# 1 <= k <= n <= 500
 

# Follow up:

# Could you solve this problem in linear time with constant space?

# Accepted
# 83.9K
# Submissions
# 107.3K
# Acceptance Rate
# 78.2%

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        # make a deque for popleft ability of size of nums from 1 to n + 1
        nums = collections.deque(range(1, n+1))
        # while you have more than one in nums, the game continues 
        while len(nums) > 1 :
            # rotate on a deque will move you to the right on a positive value 
            # think of the deque as a circular queue 
            # with 1 - k we will move to the left, but only 1 less than k steps 
            # this brings the item we want to remove to index of 0 
            '''
                    1
                5       2           Start form 
                  4   3

                    2
                1       3           rotate left 1 time 
                  5   4

                    3
                1      4            remove item at top of rotation
                    5

                    4
                3       5           rotate left one time 
                    1

                ... 

            '''
            nums.rotate(1-k)

         from collections import deque

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        arr = [i for i in range(1,n+1)]
        q = deque(arr)

        while len(q) > 1:
            for i in range(k):
                if q:
                    sel = q.popleft()
                    # print(sel, "sel", i)
                    if i != (k-1):
                        q.append(sel)
                        # print("qnow", q)
        # print(q)
        return q[0]


            # now we pop on the left, aka at the front 
            nums.popleft()
        # return the 0th item 
        return nums[0]
