# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Medium
# 1.1K
# 79
# Companies
# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

 

# Example 1:

# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
# Example 2:

# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6
# Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
 

# Constraints:

# 1 <= arr.length <= 105
# 1 <= arr[i] <= 104
# 1 <= k <= arr.length
# 0 <= threshold <= 104
# Accepted
# 55.5K
# Submissions

class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        win_start = 0
        total = 0
        count = 0

        # iterate through the array
        for win_end in range(len(arr)):
            # to the running sum, add the new number
            total += arr[win_end]

            # check if the length of the window is less than k
            if win_end - win_start + 1 < k:
                # if so, continue
                continue
            else:
                # if len of window is greater, 
                # check if the average i >= to threshold
                if (total/k) >= threshold:
                    # if so, add 1 to count
                    count+=1
                # make sure to remove the leftmost value from the total to resize the window
                total -= arr[win_start]
                # increase the index of the left value
                win_start +=1
        # return the final count
        return count
