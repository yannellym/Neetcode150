# Problem Statement #
# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

# Example 1:

# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
# Example 2:

# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        win_s = 0
        max_fruits = 0
        store = dict()

        # iterate through all fruits
        for win_e in range(len(fruits)):
            # if not in fruit, add it and add +1
            # if in fruit, add +1 
            store[fruits[win_e]] = 1 + store.get(fruits[win_e], 0)

            # if we ever have more than 2 diff types of fruit, make our window smaller
            if len(store) > 2: 
                # subtract from the fruit at index win_s of fruits
                store[fruits[win_s]] -=1
                # if the key has a value of 0, delete it
                if store[fruits[win_s]] == 0:
                    del store[fruits[win_s]]
                # increase your left index for the window
                win_s += 1
            # compare the max number of fruits you have been able to pick so far, with the running max
            max_fruits = max(max_fruits, win_e - win_s + 1)
        return max_fruits
