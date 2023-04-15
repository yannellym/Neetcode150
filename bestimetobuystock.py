# 121. Best Time to Buy and Sell Stock
# Easy

# 20290

# 652

# Add to List

# Share
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # the initial profit will equal zero to begin with
        max_prof = 0
        # set variables to iterate through our prices list
        i = 0
        j = 1
        # while our right pointer is less than the length of prices(within bounds)
        while j < len(prices):
            # see if you can make a profit 
            # if so, set our max_prof variable to this amount
            if prices[j] > prices[i]:
                max_prof = max(max_prof,prices[j] - prices[i] )
            else:
                # if you can make a profit, left i equal j so you can go right to that day.
                # you dont have to check other previous numbers as they were already visited
                i = j
            
            # increment j so you can check the next day
            j += 1
            
        return max_prof

       
       # alternative 
       
       class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        maxProf = 0

        for j in range(len(prices)) :
            if prices[j] > prices[i]:
                maxProf = max(maxProf, prices[j] - prices[i])
            else:
                i = j
            
         
      
        return maxProf
