# 226. Invert Binary Tree
# Easy
# 10.9K
# 153
# Companies
# Given the root of a binary tree, invert the tree, and return its root.

 

# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# Accepted
# 1.4M
# Submissions
# 1.9M
# Acceptance Rate
# 73.8%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if there is no root, return none
        if not root:
            return None
        # store the root.left in a temp variable
        temp = root.left
        # make root.left equal to root.right
        root.left = root.right
        # make root.right equal the temp variable that is the previous root.left
        root.right = temp

        # call the function recursively on root.left
        self.invertTree(root.left)
        # call the function recursively on root.right
        self.invertTree(root.right)
        # return the root in order to see the tree
        return root
  
     # invert means: look at every single node
         # look at its children, and swap the positions of the children
