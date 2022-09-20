# Smallest Subarray With a Greater Sum (easy)
# We'll cover the following

# Problem Statement
# Try it yourself
# Solution
# Code
# Time Complexity
# Space Complexity
# Problem Statement#
# Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

# Example 1:

# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].

# Example 2:

# Input: [2, 1, 5, 2, 8], S=7
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [8].

# Example 3:

# Input: [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to ‘8’ are [3, 4, 1] or [1, 1, 6].
  
  def smallest_subarray_sum(s, arr):
  # TODO: Write your code here
  min_length = float("inf")
  n = len(arr)
  start = 0
  end = 0
  current_sum = 0

  while end < n:
    current_sum = current_sum + arr[end]
    end += 1

    while start < end and current_sum >= s:
      current_sum -= arr[start]
      start +=1

      min_length = min(min_length, end-start + 1)
  return min_length
