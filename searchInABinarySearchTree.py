# 700. Search in a Binary Search Tree
# Easy
# 4.5K
# 163
# Companies
# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

# Example 1:


# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:


# Input: root = [4,2,7,1,3], val = 5
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 107
# root is a binary search tree.
# 1 <= val <= 107
# Accepted
# 603.4K
# Submissions
# 779.2K
# Acceptance Rate
# 77.4%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # store the root in a curr value
        curr = root

        # while there is a current 
        while curr:
            # store the current node's value in a variable
            selected = curr.val
            # if the nodes value equals the value, return the current
            if selected == val:
                return curr
            # if the nodes value is greater than the value,
            # have current equal current's left
            if selected > val:
                curr = curr.left
            # if the nodes value is less than the value,
            # have current equal current's right
            elif selected < val:
                curr = curr.right
        # if the above dont execute,this means that there is no matching node
        # return current which will be none at the end of the tree,
        return curr
  
# recusrive approach

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # if the root is none, or the value of the root equals the value
        if root is None or root.val == val:
            # return the root
            return root
        # else if the value is less than the root value, search on the left
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            # if the root value is greater than the root, search on the right
            return self.searchBST(root.right, val)
