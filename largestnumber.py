# 179. Largest Number
# Medium

# 6088

# 502

# Add to List

# Share
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

 

# Example 1:

# Input: nums = [10,2]
# Output: "210"
# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330"
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 109
# Accepted
# 363,150
# Submissions
# 1,065,564
 
def compare(x, y):
    # input type: STR
       # will compare if (first num plus second num) is greater than (Second num + first num)
    # True is equal to 1 and False is equal to 0
    if x + y > y + x:
        return -1
    return 1
        
        
class Solution:
    def largestNumber(self, nums):
        # convert each number in nums into a string by using map
        largest_num = map(str, nums)
        # sort the new array with the key being a comparison function
        # set this new array to equal the new sorted array
        largest_num = sorted(largest_num, key=cmp_to_key(compare))
        
        # join all of the strings in the largest_num array
        largest_num = ''.join(largest_num)
        # if you get an array that is ["0000"] just return 0
        return '0' if largest_num[0] == '0' else largest_num
