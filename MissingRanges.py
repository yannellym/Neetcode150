class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        ans = []
        nums.append(upper + 1)

        for num in nums:
            if lower < num:
                ans.append([lower, num - 1])
            lower = num + 1

        return ans
