# 2244. Minimum Rounds to Complete All Tasks
# Medium
# 1.9K
# 51
# Companies
# You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

 

# Example 1:

# Input: tasks = [2,2,3,3,2,4,4,4,4,4]
# Output: 4
# Explanation: To complete all the tasks, a possible plan is:
# - In the first round, you complete 3 tasks of difficulty level 2. 
# - In the second round, you complete 2 tasks of difficulty level 3. 
# - In the third round, you complete 3 tasks of difficulty level 4. 
# - In the fourth round, you complete 2 tasks of difficulty level 4.  
# It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
# Example 2:

# Input: tasks = [2,3,3]
# Output: -1
# Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.
 

# Constraints:

# 1 <= tasks.length <= 105
# 1 <= tasks[i] <= 109


class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        # creates a map to store the values in
        store = {}

        # stores all of the digits in the map
        for digit in tasks:
            store[digit] = 1 + store.get(digit, 0)
        # keep track of our count
        count = 0
        # for each value in our store ( value = the number of same difficulty level tasks)
        for value in store.values():
            # if the number of same difficulty level tasks is 1:
            # this means we cant complete it. So return -1
            if value == 1:
                return -1
            # we add to the count the amount of the value + 3 divided by 3
            # Example,  for [2,2,3,3,2,4,4,4,4,4]
            # values would equal 3, 2, 5
            # (3 + 2) = 5   5 / 3   = 1
                #(This means that 1 set of 3 can be made from the value of 5, with 1 value left over)
            # (2 + 2) = 4   4 / 3   = 1
                # (This means that 1 set of 3 can be made from the value of 4, with 1 value left over)
            # (5 + 2) = 7   7 / 3   = 2 
                #(This means that 2 sets of 3 can be made from the value of 5, with 1 value left over)
            count += (value + 2) /3
        return count
