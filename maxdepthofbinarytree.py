

# 104. Maximum Depth of Binary Tree
# Easy
# 9.5K
# 156
# Companies
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100
# Accepted
# 2.1M
# Submissions
# 2.9M
# Acceptance Rate
# 73.4%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        res = []
        self.depth(root, 0,res)
        return max(res)

        
    def depth(self, node, count,res):
        if not node:
            res.append(count)
            return
        self.depth(node.right, count+1,res)
        self.depth(node.left, count+1,res)

        # more concise

        # def dfs(root, depth):
        #     if not root: return depth
        #     return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                       
        # return dfs(root, 0)
