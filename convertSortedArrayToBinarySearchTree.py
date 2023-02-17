# 108. Convert Sorted Array to Binary Search Tree
# Easy
# 9.1K
# 459
# Companies
# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.

 

# Example 1:


# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:


# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.
# Accepted
# 949.5K
# Submissions
# 1.4M
# Acceptance Rate
# 69.6%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(l, r):
            # if the left is greater than the right, we need to stop
            if l > r:
                # just return None
                return None
            # we start at the middle, by taking the left+ right and doing digit division
            middle = (l+r) // 2
            # create a root by creating a node with the middle value of the list
            root = TreeNode(nums[middle])
            # call helpfer func on left, and middle - 1 to create a root.left
            root.left = helper(l,middle-1)
            # call helpfer func on middle+1, and right to create a root.right
            root.right = helper(middle+1, r)
            
            return root


        # call the helper func starting at 0 (L) and ending at len(nums)-1 (R)
        return helper(0, len(nums)-1)
