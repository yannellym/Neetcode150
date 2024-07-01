1248. Count Number of Nice Subarrays
Solved
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
Seen this question in a real interview before?
1/5
Yes
No
Accepted
250.4K
Submissions
352.9K
Acceptance Rate
71.0%

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total_subcount = 0
        store = {0:1}
        running_odd_count = 0

        for num in nums:
            # if its odd, add to our running odd count
            if num % 2:
                running_odd_count += 1

            # if our running odd count - k is in store
            if (running_odd_count - k) in store:
                total_subcount += store[(running_odd_count)-k]
            
            # if the odd count is in our store:add 1 else add it
            if running_odd_count in store:
                store[running_odd_count] += 1
            else:
                store[running_odd_count] = 1
                
        return total_subcount

