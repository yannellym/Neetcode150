# 102. Binary Tree Level Order Traversal
# Medium
# 12K
# 234
# Companies
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
# Accepted
# 1.6M
# Submissions
# 2.6M
# Acceptance Rate
# 63.7%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # create a queue
        # if the root is none, return []

        queue = deque([root] if root else [])
        ans = []

        # while there is a queue
        while len(queue):
            qlength = len(queue)
            row = []
            # for every element in the queue
            for _ in range(qlength):
                # pop the element on the left
                curr = queue.popleft()
                # append it to the row array
                row.append(curr.val)
                # if the current node has a left child, add it to the queue
                if curr.left: 
                    queue.append(curr.left)
                # if the current node has a right child, add it to the queue
                if curr.right: queue.append(curr.right)
            #append the row to the answer
            ans.append(row)
        return ans
