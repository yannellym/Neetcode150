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

def fruitsbaskets(arr):
  res = 0
  store = {}
  win_start = 0
  for win_end in range(len(arr)):
    right_char = arr[win_end]
    if right_char not in store:
      store[right_char] = 0
    store[right_char] += 1

    while len(store) > 2:
      left_char = arr[win_start]
      store[left_char] -= 1
      if store[left_char] == 0:
        del store[left_char]
      win_start += 1
    res = max(res, win_end - win_start + 1)
  return res



fruitsbaskets(['A', 'B', 'C', 'B', 'B', 'C'])
  
