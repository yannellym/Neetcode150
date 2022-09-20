# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  n = len(arr)

  if n < k: 
    return -1
  
  window_sum = sum(arr[:k])
  max_sum = window_sum

  for i in range(n-k):
    window_sum = window_sum - arr[i] + arr[i+k]
    max_sum = max(window_sum, max_sum)
  return max_sum
