# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# Easy
# 1.5K
# 1.8K
# Companies
# Given two binary trees original and cloned and given a reference to a node target in the original tree.

# The cloned tree is a copy of the original tree.

# Return a reference to the same node in the cloned tree.

# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

 

# Example 1:


# Input: tree = [7,4,3,null,null,6,19], target = 3
# Output: 3
# Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
# Example 2:


# Input: tree = [7], target =  7
# Output: 7
# Example 3:


# Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
# Output: 4
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# The values of the nodes of the tree are unique.
# target node is a node from the original tree and is not null.
 

# Follow up: Could you solve the problem if repeated values on the tree are allowed?

# Accepted
# 184.7K
# Submissions
# 212.8K
# Acceptance Rate
# 86.8%
# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Related Topics
# Copyright ©️ 2023 LeetCode All rights reserved

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        def search(org_node,copy_t):
            # if there's not an original node, return 
            if not org_node:
                return
            # if the original node val == the target.val, return the node in copy
            elif org_node.val == target.val:
                return copy_t
            # recursively call search on org.left, and copy.left and viseversa for the right side
            return search(org_node.left, copy_t.left) or search(org_node.right, copy_t.right)
        # return the result of calling search on the original and cloned
        return search(original, cloned)

