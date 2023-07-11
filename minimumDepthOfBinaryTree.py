# 111. Minimum Depth of Binary Tree
# Easy
# 6.6K
# 1.2K
# company
# Amazon
# company
# Facebook
# company
# Bloomberg
# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
 

# Constraints:

# The number of nodes in the tree is in the range [0, 105].
# -1000 <= Node.val <= 1000
# Accepted
# 1M
# Submissions
# 2.2M
# Acceptance Rate
# 46.0%


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return self.minDepth(root.right) + 1

        if root.right is None:
            return self.minDepth(root.left) + 1

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        return min(left_depth, right_depth) + 1
       

# If the root node is empty (null), the tree has no depth, so return 0.

# If both the left and right child of the root node are empty (null), the tree has a depth of 1 since the root node itself is a leaf. Return 1.

# If the left child is empty (null), recursively calculate the minimum depth of the right subtree and add 1 to it. Return this value.

# If the right child is empty (null), recursively calculate the minimum depth of the left subtree and add 1 to it. Return this value.

# If both the left and right child are not empty, recursively calculate the minimum depth of both subtrees. Take the minimum of these two depths and add 1 to it. Return this value
