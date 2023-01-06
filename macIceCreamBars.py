# 1833. Maximum Ice Cream Bars
# Medium
# 1.6K
# 570
# Companies
# It is a sweltering summer day, and a boy wants to buy some ice cream bars.

# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

# Return the maximum number of ice cream bars the boy can buy with coins coins.

# Note: The boy can buy the ice cream bars in any order.

 

# Example 1:

# Input: costs = [1,3,2,4,1], coins = 7
# Output: 4
# Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
# Example 2:

# Input: costs = [10,6,8,7,7,8], coins = 5
# Output: 0
# Explanation: The boy cannot afford any of the ice cream bars.
# Example 3:

# Input: costs = [1,6,3,1,2,5], coins = 20
# Output: 6
# Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.
 

# Constraints:

# costs.length == n
# 1 <= n <= 105
# 1 <= costs[i] <= 105
# 1 <= coins <= 108

class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        # declare the length of the costs arr
        n = len(costs)
        # if the length of the costs arr is 0, or coins is 0, return 0
        if n == 0 or coins == 0:
            return 0
        # sort the costs arr
        costs.sort()
        # declare a sum variable
        summ = 0
        # create a window that keeps track of the sum of the cost of the icecream bars
        for i in range(len(costs)):
            summ += costs[i]
        # if the sum equals the amount of coins the child has,
        # return the length of the window or index + 1
            if summ == coins:
                return i + 1
        # if the summ is greater than the coins the child has
        # return the index
            elif summ > coins:
                return i
        # if we reach the end of the array
        # return n as we can afford all the icecream bars!
            elif i == n-1:
                return n
            
            
            # approach 2
            
            class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        bars=0
        for i in costs:
            if i<=coins:
                bars += 1
                coins -= i
        return bars
