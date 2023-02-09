# 617. Merge Two Binary Trees
# Easy
# 7.8K
# 272
# Companies
# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

 

# Example 1:


# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
# Example 2:

# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
 

# Constraints:

# The number of nodes in both trees is in the range [0, 2000].
# -104 <= Node.val <= 104
# Accepted
# 659.9K
# Submissions
# 839.4K
# Acceptance Rate
# 78.6%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """


        # if there's not a node on the root1, return node on root2
        if not root1:
            return root2
        # if there's not a node on the root2, return node on root1
        if not root2:
            return root1
        # creaste a tree node with the values of the nodes from root1 and root2
        t = TreeNode(root1.val+root2.val)

        # recursively assign the left values to the tree by calling root1.left and root2.left
        t.left = self.mergeTrees(root1.left, root2.left)
         # recursively assign the right values to the tree by calling root1.right and root2.right
        t.right = self.mergeTrees(root1.right, root2.right)
        #return the root
        return t


    
