# 605. Can Place Flowers
# Easy

# 3311

# 696

# Add to List

# Share
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 

# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length
# Accepted
# 329,736
# Submissions
# 1,001,996

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
       # lets assume that the left and right sides of this array are 0s
       # [0,1,0,0,0,1,0]
      
        new_arr = [0] + flowerbed + [0]
        for i in range(1, len(new_arr) -1):
          # check in chunks of 3, if the entire chunk is [0,0,0], we can plant a flower.
            if new_arr[i-1] == 0 and new_arr[i] == 0 and new_arr[i + 1] == 0:
                # make the ith place equal one. Thus, planting a flower
                new_arr[i] = 1
                # decrease n. This will allow us to see if we can plant nth flowers.
                n -= 1
        # if n is less than or equal to 0, it means that we planted all of the flowers that were given to us.
        return n <= 0
