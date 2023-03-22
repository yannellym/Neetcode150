#  Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique. 

def topKFrequent(self, nums, k):
        c = Counter(nums)
        return [key for key, val in c.most_common(k)]
  
  
  # better approach
  
    # creates a counter of nums
        n = Counter(nums) 
        # sorts the counter by the following rules:
        # for every value, sort it in descending order with values that have the most first
        n = sorted(n, key = lambda x: -n[x])
        # return up to k because those are the top k values
        return n[:k]
