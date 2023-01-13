# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.
# Accepted
# 1.1M
# Submissions
# 1.8M
# Acceptance Rate
# 60.8%


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # store the root in a variable to be able to iterate through the tree
        current = root
        # while there is a current (we have a node)
        while current:
            # if both values are greater than our current node
              # this means that we're looking at the RIGHT side of our tree.
              # we need to keep looking down the right side 
              # to iterate, make the current equal the current.right
            if p.val > current.val and q.val > current.val:
                current = current.right
             # if both values are less than our current node
              # this means that we're looking at the LEFT side of our tree.
              # we need to keep looking down the left side 
              # to iterate, make the current equal the current.left
            elif p.val < current.val and q.val <current.val:
                current = current.left
            # if we make it to this point, it means we found the answer
              # the tree is either split and we're returning the parent node OR
              # one of the nodes is a descendant of itself
            else:
                return current
            
