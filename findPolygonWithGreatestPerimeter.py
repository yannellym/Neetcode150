2971. Find Polygon With the Largest Perimeter
Solved
Medium
Topics
Companies
Hint
You are given an array of positive integers nums of length n.

A polygon is a closed plane figure that has at least 3 sides. The longest side of a polygon is smaller than the sum of its other sides.

Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak, then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.

The perimeter of a polygon is the sum of lengths of its sides.

Return the largest possible perimeter of a polygon whose sides can be formed from nums, or -1 if it is not possible to create a polygon.

 

Example 1:

Input: nums = [5,5,5]
Output: 15
Explanation: The only possible polygon that can be made from nums has 3 sides: 5, 5, and 5. The perimeter is 5 + 5 + 5 = 15.
Example 2:

Input: nums = [1,12,1,2,5,50,3]
Output: 12
Explanation: The polygon with the largest perimeter which can be made from nums has 5 sides: 1, 1, 2, 3, and 5. The perimeter is 1 + 1 + 2 + 3 + 5 = 12.
We cannot have a polygon with either 12 or 50 as the longest side because it is not possible to include 2 or more smaller sides that have a greater sum than either of them.
It can be shown that the largest possible perimeter is 12.
Example 3:

Input: nums = [5,5,50]
Output: -1
Explanation: There is no possible way to form a polygon from nums, as a polygon has at least 3 sides and 50 > 5 + 5.
 

Constraints:

3 <= n <= 105
1 <= nums[i] <= 109
Seen this question in a real interview before?
1/4
Yes
No
Accepted
16.1K
Submissions
31.9K
Acceptance Rate
50.6%


class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Return the largest possible perimeter of a polygon whose sides can be formed from nums, 
        # or -1 if it is not possible to create a polygon.

        # sort in reverse order so the biggest are first
        nums.sort()
        
        # the total sum of the array so we dont need to keep computing
        total = sum(nums)
        # keep track of the curr_sum (values we add starting from the right end)
        curr_sum = 0

        # starting in reverse
        for i in range(len(nums)-1,-1,-1):
            # lets add the curr num to curr_sum 
            curr_sum += nums[i]
            # remaining will basically be our sum of the left, total - curr_sum
            remaining = total - curr_sum

            # if the remaining is greater than the curr num
            if remaining > nums[i]:
                # we return remaining plus nums[i]
                return remaining + nums[i]
        # if we dont find anything, we return -1 
        return -1
        
        # ex: [1,12,1,2,5,50,3]
        '''
        1.  sort [1,1,2,3,5,12,50]
        2.  total  = 74 
        3.  iterate in reverse - 
        4.  curr_sum = 50    remaining = 74-50 =34   remaining > nums[i]? 34 > 50 NO
        5.  curr_sum = 62    remaining = 74-62 =12   remaining > nums[i]? 12 > 12 NO
        6.  curr_sum = 67    remaining = 74-67 = 7   remaining > nums[i]? 7 > 5 YES return 7 + 5

        '''
        
