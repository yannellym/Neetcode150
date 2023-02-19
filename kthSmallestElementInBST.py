# 230. Kth Smallest Element in a BST
# Medium
# 9.3K
# 165
# Companies
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

# Accepted
# 1M
# Submissions
# 1.5M
# Acceptance Rate
# 69.9%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        values = []
        
        def bfs(node):
            if not node:
                return None
            values.append(node.val)
            bfs(node.left)
            bfs(node.right)
        bfs(root)
        return sorted(values)[k-1]
      
      # iterativeclass Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        index = 0
        stack = []
        curr = root

        # while we have a stack or a current
        while curr or stack:
            # while there is a current
            while curr:
                # append the current node to the stack
                stack.append(curr)
                # keep going left
                curr = curr.left
            # pop the last element of the stack
            # this should be the uttermost left value of the tree at first
            curr = stack.pop() 
            # increase the index 
            index += 1

            # if the index equals k: return it
            if index == k:
                return curr.val
            # if we dont find it above, go through the tree's right values
            curr = curr.right
