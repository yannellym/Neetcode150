645. Set Mismatch
Solved
Easy
Topics
Companies
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
 

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
Seen this question in a real interview before?
1/4
Yes
No
Accepted
305K
Submissions
715.6K
Acceptance Rate
42.6%

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        # create a set s containing all numbers from 1 to the length of the input array nums
        s = set(range(1, len(nums) + 1))
        duplicate = 0

        for num in nums:
            if num not in s:
            # Check if the current element i is not in the set s. 
            # If true, it means that i is the repeated number,
                duplicate = num
            else:
                s.remove(num)
        return [duplicate, list(s).pop()]
        # duplicate variable holds the repeated number, 
        # and list(s).pop() extracts and returns the missing number from the set.
