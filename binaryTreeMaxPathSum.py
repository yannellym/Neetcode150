# 124. Binary Tree Maximum Path Sum
# Hard
# 15.2K
# 667
# company
# Citadel
# company
# Amazon
# company
# Apple
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:


# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 3 * 104].
# -1000 <= Node.val <= 1000
# Accepted
# 1M
# Submissions
# 2.6M
# Acceptance Rate
# 39.4%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.max_sum = float('-inf')  # Initialize the maximum sum
        
        def maxPathSumHelper(node):
            if not node:
                return 0
            
            # Calculate maximum path sums for left and right 
            # they could be negative so this is why we use 0
            left_sum = max(0, maxPathSumHelper(node.left))
            right_sum = max(0, maxPathSumHelper(node.right))
            
            # Calculate the maximum path sum including the current node
            current_sum = node.val + left_sum + right_sum
            
            # Update the global maximum sum if necessary
            self.max_sum = max(self.max_sum, current_sum)
            
            # Return the maximum path sum that can be extended further up
            return node.val + max(left_sum, right_sum)
        
        maxPathSumHelper(root)  # Start the recursion
        return self.max_sum
