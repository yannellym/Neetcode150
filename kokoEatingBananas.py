# 875. Koko Eating Bananas
# Medium
# 7K
# 325
# Companies
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 

# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109
# Accepted
# 320.8K
# Submissions
# 614.6K
# Acceptance Rate
# 52.2%

import math 
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        # approach: pick the maximum number of the piles arr
        # create a range from 1 (the least amount of banans we can eat) to max off piles arr
        # do a binary search and update the hours var to be the min value when you divide each pile by the 
        # selected value of the range
      

        # the min quantity of bananas we can eat
        l = 1
        # the max value of bananas we can eat based on the max of the piles list
        r = max(piles)
        #. set j to the max of the piles since this is the max amount of hours we can take
        res = r

        # perform the binary search
        while l <= r:
            # get the middle value of the range
            k = (l+r) // 2
            # declare our hours variable to keep track of the hours
            hours = 0
            for pile in piles:
                # to the hours var add the result of diving the quantity of the pile by the mid value rounded UP
                # this will assure that you account for the left overs
                # convert pile to a float in order to be able to round up
                hours +=  math.ceil(float(pile) / k)
            # if the hours are less than or equal to h(our max hours)
            if hours <= h:
                # set the res to be the min between res and K(our middle value)
                res = min(res,k)
                # decrease our right value pointer to be middle minus 1
                # we don't need to look at those values now since we want to find a smaller value
                r = k-1
            else:
                # if the hours are greater than h, increase our left pointer to be middle plus 1
                # our rate of eating bananas was too small, so we need to increase it
                l= k + 1
        return res

        # for every pile, coco will try to eat # bananas in k hours.
        '''
        Input: piles = [3,6,7,11], h = 8
        Output: 4
        
        for hour 1, she eats 3
        hour 2, eats 4
        hour 3, eats the remaining 2 from the pile
        hour 4, eats 4 
        hour 5, eats the reamining 3 from pile
        hour 6, eats 4
        hour 7, eats 4
        hour 8, eats 3 remaining from pile.
        '''
