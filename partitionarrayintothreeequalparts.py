# 1013. Partition Array Into Three Parts With Equal Sum
# Easy
# 1.4K
# 134
# Companies
# Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

# Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

 

# Example 1:

# Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# Example 2:

# Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
# Example 3:

# Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

# Constraints:

# 3 <= arr.length <= 5 * 104
# -104 <= arr[i] <= 104
# Accepted
# 74.9K
# Submissions
# 174.3K
# Acceptance Rate
# 43.0%


class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        
        # get the sum of the array
        n = sum(arr) 
        # if it is not divisible by 3, it cannot be parted into 3
        if n % 3:
            return False

        sums = 0
        count = 0
        # go through each num in the array
        for num in arr:
          # add it to sums
            sums += num
            # if the sum is equal to 1/3 of the sum of the aray
            if sums == (n//3):
              # add one to the counter and have sums equal 0
                count += 1
                sums = 0
            # if count equals 3, that means it can be partitioned into 3, return true
            if count == 3:
                return True
        # else, return false
        return False


        
