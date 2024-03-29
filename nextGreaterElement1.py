# 496. Next Greater Element I
# Easy
# 5.8K
# 392
# Companies
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

# Example 1:

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# Example 2:

# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

# Constraints:

# 1 <= nums1.length <= nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 104
# All integers in nums1 and nums2 are unique.
# All the integers of nums1 also appear in nums2.
 

# Follow up: Could you find an O(nums1.length + nums2.length) solution?
# Accepted
# 505K
# Submissions
# 707K
# Acceptance Rate
# 71.4%


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
    

        dict = { value:index for index,value in enumerate(nums1)}
        res = [-1] * len(nums1)
        # look through nums2
        for i in range(len(nums2)):
            # if the digit at the current index of nums2 is not in nums1, continue
            if nums2[i] not in nums1:
                continue
            # for every digit in the subarray of nums2[digit+1]
            for j in nums2[i+1:]:
                # if j is greater than nums2[i](digit)
                if j > nums2[i]:
                    # make the target equal the number saved in the dict of nums2[i]
                    target = dict[nums2[i]]
                    # the position of target in res will equal j
                    res[target] = j
                    # break so it doesnt continue looking
                    break
        return res

        # value: index
        # dict = {4: 0, 1:1, 2:2}

        # steps:

        # the the value and the index on a dict
        # search through nums2,
          # if the value in the current index of nums2 is NOT in nums1: continue
        # for every j in the subarray of nums2[i+1:]:
          # if the j is greater than nums2[i]:
            # declare a var that is equal to nums2[i] in dict. This will be called target. It will be the index of the num

            # change res' index that is equal to target to be J
            # break so we dont continue looking
        # return the res
