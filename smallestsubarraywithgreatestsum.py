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
  subarr_len = float('inf')
  win_start = 0
  win_sum = 0
  for win_end in range(len(arr)):
    win_sum += arr[win_end]
    while win_sum >= s:
      subarr_len = min(subarr_len, len(arr[win_start:win_end + 1]))
      win_sum -= arr[win_start]
      win_start += 1
  
  return subarr_len
