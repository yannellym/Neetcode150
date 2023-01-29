# 94. Binary Tree Inorder Traversal
# Easy
# 10.7K
# 515
# Companies
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?
# Accepted
# 1.9M
# Submissions
# 2.6M
# Acceptance Rate
# 73.5%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # this output will hold our nodes
        output = []
        # call the recursive function and provide the root and the output array
        self.inorder(root,output)
        #  Lastly, return the array
        return output
        
    # helper function
    def inorder(self, node, output):
        # if there no node, just return
        # in this case, it will exit the function and return the output array
        if not node: 
            return
        # look through all of the nodes on the left
        self.inorder(node.left, output)
        # append the middle value to the output array   
        output.append(node.val)
        # look through all of the nodes on the right
        self.inorder(node.right, output)
    
