# 103. Binary Tree Zigzag Level Order Traversal
# Medium
# 8.1K
# 212
# Companies
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
# Accepted
# 869.7K
# Submissions
# 1.6M
# Acceptance Rate
# 55.6%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # if the root is empty, return the root
        if not root: return []

        # create a deque
        queue = collections.deque([root])
        # create a list for our response
        res = []
        # initialize the first level to odd
        even_level = False

        # while we have a Q
        while queue:
            # get the length of the Q
            n = len(queue)
            # create our level sublist
            level = []
            # loop as many times as we have elements in our Q
            for i in range(n):
                # if the level is even
                if even_level:
                    # pop from right and append from left.
                    node = queue.pop()
                    # to maintain the order of nodes in the format of [left, right, left, right] 
                    # we push right first since we are appending from left
                    if node.right: queue.appendleft(node.right)
                    if node.left: queue.appendleft(node.left)
                else:
                    # pop from left and append from right
                    node = queue.popleft()
                    # here the order is maintained in the format [left, right, left, right] 
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                level.append(node.val)
            res.append(level)
            even_level = not even_level
	return res

                
