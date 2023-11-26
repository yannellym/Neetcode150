1685. Sum of Absolute Differences in a Sorted Array
Solved
Medium
Topics
Companies
Hint
You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

 

Example 1:

Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
Example 2:

Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]
 

Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= nums[i + 1] <= 104
Seen this question in a real interview before?
1/4
Yes
No
Accepted
93.6K
Submissions
135.1K
Acceptance Rate
69.3%

class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        # Calculate the total sum of the array
        total_sum = sum(nums)

        # Initialize left_sum and right_sum
        left_sum = 0
        right_sum = total_sum

        # Initialize result array
        result = [0] * n

        for i in range(n):
            # Calculate the sum of absolute differences for the current element

            # Contribution from elements to the left
            left_contribution = i * nums[i] - left_sum

            # Contribution from elements to the right
            right_contribution = right_sum - ((n - i) * nums[i])

            # Calculate the total sum of absolute differences for the current element
            result[i] = left_contribution + right_contribution

            # Print intermediate result (for debugging purposes)
            print(result)

            # Update left_sum (sum of elements to the left of nums[i])
            left_sum += nums[i]

            # Update right_sum (sum of elements to the right of nums[i])
            right_sum -= nums[i]

        return result
