# 110. Balanced Binary Tree
# Easy
# 9.5K
# 536
# company
# Amazon
# company
# Facebook
# company
# Adobe
# Given a binary tree, determine if it is 
# height-balanced
# .

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104
# Accepted
# 1.2M
# Submissions
# 2.4M
# Acceptance Rate
# 49.9%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Helper function to calculate the height of a node
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)  # Calculate height of the left subtree
            right_height = height(node.right)  # Calculate height of the right subtree
            return 1 + max(left_height, right_height)  # Return the height of the node

        # Helper function to check if the tree is balanced
        def is_balanced_helper(node):
            if not node:
                return True

            # Calculate the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)

            # Check if the difference in height between left and right subtrees is more than 1
            if abs(left_height - right_height) > 1:
                return False  # If it's more than 1, the tree is not balanced

            # Recursively check if the left and right subtrees are balanced
            return is_balanced_helper(node.left) and is_balanced_helper(node.right)

        # Call the helper function to check if the tree is balanced
        return is_balanced_helper(root)
