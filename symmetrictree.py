# 101. Symmetric Tree
# Easy
# 12.1K
# 274
# Companies
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if there is no root, return true
        # this is still a valid binary tree
        if root is None:
            return True
        # return the result of calling isMirror function on root.left, and root.right
        return self.isMirror(root.left, root.right)

    # helper function to recursively figure out if the tree mirrors itself
    def isMirror(self, left: TreeNode | None, right: TreeNode | None) -> bool:
        # if both of the trees are done or there are no trees on either side,
        # return true as they mirror each other
        if left is None and right is None:
            return True
        # if the left tree is None or the right tree is None,
        # one side of the tree is shorter than the other,
        # return false as they don't mirror each other
        if left is None or right is None:
            return False
        # if the left value doesnt equal the right value,
        # return false as they are not the same. They dont mirror each other
        if left.val != right.val:
            return False
        # if it got to this point, this means that its good so far and we need
        # to check the following nodes by calling the left of the left& the right of the right
        #AND check the following nodes by calling the right of left & left of right
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
