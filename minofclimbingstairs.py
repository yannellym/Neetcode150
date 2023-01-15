# 746. Min Cost Climbing Stairs
# Easy
# 8.7K
# 1.3K
# Companies
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

 

# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
 

# Constraints:

# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # appends 0 to end of array since the cost at that point would be 0 
        cost.append(0)
        # start at the third position starting from end of array'
        # iterate backwards
        for i in range(len(cost)-3, -1, -1):
            # modify cost[i] to equal the min between the one before or two before
            cost[i] += min(cost[i+1], cost[i+2])
        #return the min value of either cost 0 or cost 1
        return min(cost[0], cost[1])
