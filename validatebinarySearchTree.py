# 98. Validate Binary Search Tree
# Medium
# 13.6K
# 1.1K
# Companies
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValid(node, left, right):
            # even if the tree is empty, it's still a binary tree
            if not node:
                return True
            # if The left subtree of a node contains only nodes with keys less than the node's key AND
            # The right subtree of a node contains only nodes with keys greater than the node's key.
            # THEN, its a binary tree
            if not(node.val > left and node.val < right):
                # if it doesnt meet the conditions above, return False. It's not a binary tree
                return False
            # if it gets to here, its because its a binary tree, THUS FAR
            # ITERATE THROUGH THE NEXT SET OF NODES
            # replace the node for the node's left value, and the right for the parent.node's val
            # replace the node for the node's right value, and the left for the parent.node's val
            return (isValid(node.left, left, node.val) and isValid(node.right, node.val, right))
        # you begin the call by passing in the root, and the infinity values 
        # as they can be anything between -inf and positive inf
        return isValid(root, float('-inf'), float('inf'))
