# 739. Daily Temperatures
# Medium
# 10.5K
# 236
# Companies
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100
# Accepted
# 604.1K
# Submissions
# 911.8K
# Acceptance Rate
# 66.3%

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(temperatures)
        
        # enumerate temperatures so you can get the index and the temp
        for i, temp in enumerate(temperatures):
            # while there is a stack and the temp in the stack is less than the curr temp (we're good)
            while stack and stack[-1][0] < temp:
                # get the temp, and index while popping it from the stack
                ntemp, nidx = stack.pop()
                # set that temp in your res arr to equal the diff between the index of the curr temp and the nidx
                res[nidx] = (i-nidx)
            # at the end, add you new temp to the res along with the index
            stack.append([temp, i])
        return res


      
