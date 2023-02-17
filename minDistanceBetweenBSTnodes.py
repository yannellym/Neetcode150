# 783. Minimum Distance Between BST Nodes
# Easy
# 2.9K
# 384
# Companies
# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 100].
# 0 <= Node.val <= 105
 

# Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Accepted
# 198.3K
# Submissions
# 335.6K
# Acceptance Rate
# 59.1%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # set prev to initially equal None as we haven't seen a node yet
        prev = None
        # make res a positive infinity value
        res = float('inf')

        # helper function for depth first search
        def dfs(node):
            # if there's not a node, just return
            if not node:
                return
            # declare prev and res to be nonlocal since these vars are outside of the func
            nonlocal prev, res
            # call dfs on node.left
            dfs(node.left)
            # if there's a previous
            if prev:
                # have the res equal to the min between res and (node.val - prev.val)
                res = min(res, node.val - prev.val)
            # update the prev to equal the node since we have one now
            prev = node
            # call dfs on node.right
            dfs(node.right)
        # call dfs on the root
        dfs(root)
        # return the res that has been modified. 
        return res
