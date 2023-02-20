# 236. Lowest Common Ancestor of a Binary Tree
# Medium
# 13.5K
# 324
# Companies
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.
# Accepted
# 1.3M
# Submissions
# 2.1M
# Acceptance Rate
# 58.6

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
    
        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)

        if left_res and right_res:
            return root
        return left_res or right_res

#         The algorithm takes in three parameters: root, p, and q, where root is the root
        # node of a binary tree, and p and q are two distinct nodes in the same binary tree.

            # If the current root is None or if it is the same as p or q, then the algorithm 
            # returns the root itself as it is either the LCA (lowest common ancestor) or one of the 
            # nodes p or q.

            # If root is not None and not equal to p or q, the algorithm recursively calls 
            # lowestCommonAncestor() on the left and right subtrees of the current root.
     

            # The returned value from calling lowestCommonAncestor() on the left subtree is stored in the variable 
            # left_res, and the returned value from calling lowestCommonAncestor() on the right subtree is stored 
            # in the variable right_res.

            # If left_res and right_res are both non-null, this means that p and q are both present in different 
            # subtrees of the current root. In this case, the current root is the LCA, and the algorithm returns the root.

            # If either left_res or right_res is non-null, this means that either p or q is present in the corresponding 
            # subtree, and the other node is either in the other subtree or not present in the tree at all. In this case,
            # the algorithm returns the non-null value from left_res or right_res, which is the LCA of p and q in that subtree.

            # If both left_res and right_res are null, then neither p nor q is present in the current subtree, and the
            #  algorithm returns None. This step is not explicitly mentioned in the code but is implied by the fact that
            #  if left_res and right_res are both null, the function returns None by default.

