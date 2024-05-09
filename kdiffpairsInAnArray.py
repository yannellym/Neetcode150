532. K-diff Pairs in an Array
Medium
Topics
Companies
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

 

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
 

Constraints:

1 <= nums.length <= 104
-107 <= nums[i] <= 107
0 <= k <= 107

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # if its less than 0, we just return 0
        if k < 0:
            return 0
        
        store = {}
        res = set()
        
        # if k is 0, 
        if k == 0:
            # we create a count of how many times each number in nums appears
            for num in nums:
                store[num] = store.get(num, 0) + 1
            # we return the sum of the numbers that appear more than once in our store
            # ex, 1-1=0, 4-4 =0
            return sum(1 for num, freq in store.items() if freq >= 2)
        
        for num in nums:
            # find the number that you need
            need = abs(num - k)
            if need in store:
                # if the pair is in the store, add it to our res
                res.add((num, need))
            # add the num and what we need to our store
            store[num] = need + store.get(num, 0)
        
        return len(res)
