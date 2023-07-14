# 112. Path Sum
# Easy
# 7.8K
# 912
# Companies
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.
# Example 3:

# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
# Accepted
# 1.1M
# Submissions
# 2.3M
# Acceptance Rate


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # create a helpher function to do depth first search
        def dfs(node, curSum):
            # if there is no node, return False as theres no path to equal the targetSum
            if not node:
                return False
            # add the node value to the currSum
            curSum += node.val
            # if the node is a leaf (no node to the left, no node to the right)
            if not node.left and not node.right:
                # return if the current sum equals the target sum
                return curSum == targetSum
            # recursively call dfs on node.left, pass in the curSum
            # recursively call dfs on node.right, pass in the curSum
            # if either comes back positive, return that
            return (dfs(node.left, curSum) or dfs(node.right, curSum))
        # call your helper function
        return dfs(root, 0)


# alternative 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # if there's no root, return False
        if root is None:
            return False
        # if the node is a leaf node, check if the value is equal to targetSum
        # You;re on the last node and it hasn't been subtracted yet so if there;s a path sum
        # targetSym and root.val will equal each other
        if root.left is None and root.right is None:
            return targetSum == root.val

        # return if either one is true. 
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
