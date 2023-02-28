# 257. Binary Tree Paths
# Easy
# 5.5K
# 236
# Companies
# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:

# Input: root = [1]
# Output: ["1"]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
# Accepted
# 599.8K
# Submissions
# 979.9K
# Acceptance Rate

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # if there's no root, return []
        if not root:
            return []
        # paths arr to keep our final annswer 
        paths = []
        # helper func dfs. Pass in node, and path
        def dfs(node, path):
            # if its a leaf node, no .left and no.right
            if not node.left and not node.right:
                # append the path to our paths
                paths.append(path)
            # if there's a node.left
            if node.left:
                # calls dfs on the node.left and to the path add -> and a string of node.left.val
                dfs(node.left, path + "->" + str(node.left.val))
            # if there's a node.right
            if node.right:
                # calls dfs on the node.right and to the path add -> and a string of node.right.val
                dfs(node.right, path + "->" + str(node.right.val))
        # call the helpfer func, pass in the root and a str of the root.val
        dfs(root, str(root.val))
        # return the paths arr
        return paths

# 61.2%
