# 1313. Decompress Run-Length Encoded List
# Easy
# 971
# 1.2K
# Companies
# We are given a list nums of integers representing a list compressed with run-length encoding.

# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

# Return the decompressed list.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]
# Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
# The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
# At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
# Example 2:

# Input: nums = [1,1,2,3]
# Output: [1,3,3]
 

# Constraints:

# 2 <= nums.length <= 100
# nums.length % 2 == 0
# 1 <= nums[i] <= 100

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        declare i and j: i = 0, 1
        create a variables res to hold the resulting list
        make a sliding window that holds its length
        save nums 0 on a variable called freq
        save nums 1 on a variable called val

        create a while loop that loops freq amount of time:
        add val to res

        update i +2 and j + 2
        """

        i = 0
        j = 1
        res = []

        while j < len(nums):
            window = nums[i:j+1]
            freq = window[0]
            val = window[1]

            for k in range(freq):
                res.append(val)
            i += 2 
            j += 2
        return res
      
      
      # second solution
      
      class Solution:
        def decompressRLElist(self, nums: List[int]) -> List[int]:
            a=[]
            for i in range(1,len(nums),2):
                a.extend([nums[i]]*nums[i-1])
            return a
