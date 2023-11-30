# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium
# 12.2K
# 359
# Companies
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
# Accepted
# 926.5K
# Submissions
# 1.5M
# Acceptance Rate
# 61.3%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root


# preorder ALWAYS has the node first. But you don't know the size of either branch.
# inorder ALWAYS has the left branch to the left of the node, and right branch right of the node. So now you know the size of each branch.
# Take those information and break the arrays into subproblems, based on the size.  



# Assuming we have a preorder traversal list [3, 9, 20, 15, 7] and an inorder traversal list [9, 3, 15, 20, 7], the root node will be 3.

# First, we create a new TreeNode object with the value of preorder[0], which is 3. This is the root of the entire tree.
# We find the index of 3 in the inorder list. It is at index 1. This divides the inorder list into [9] (left subtree) and [15, 20, 7] (right subtree).
# We construct the left subtree using the sublist of preorder from the second element to mid+1, and the sublist of inorder from the beginning to mid. This means that the left subtree will be constructed using the preorder traversal list [9] and the inorder traversal list [9]. We repeat the process for this left subtree, and the recursive call becomes self.buildTree([9], [9]). This call will return a new TreeNode object with the value of 9. We set root.left to this new TreeNode object.
# We construct the right subtree using the sublist of preorder from mid+1 to the end, and the sublist of inorder from mid+1 to the end. This means that the right subtree will be constructed using the preorder traversal list [20, 15, 7] and the inorder traversal list [15, 20, 7]. We repeat the process for this right subtree, and the recursive call becomes self.buildTree([20, 15, 7], [15, 20, 7]). This call will construct the subtree rooted at 20, and return a new TreeNode object with the value of 20. We set root.right to this new TreeNode object.
# We return the root node with the entire tree constructed.

# https://www.youtube.com/watch?v=ihj4IQGZ2zc&t=1s&ab_channel=NeetCode


# better explained 

  # Base case: if either the preorder or inorder list is empty, return None
        if not preorder or not inorder:
            return None
        
        # Create a root node with the value of the first element in the preorder list
        root = TreeNode(preorder[0])
        
        # Find the index of the root value in the inorder list
        mid = inorder.index(preorder[0])
        
        # Recursive approach:
        # The left subtree will be constructed from elements in preorder[1:mid+1] and inorder[:mid]
        # For example, if preorder is [3, 9, 20, 15, 7] and mid is 1 (root value 9 in the 
        # inorder list), then preorder[1:mid+1] would result in [9], which represents the
        #    values in the left subtree of the binary tree rooted at 9.
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid+1])
        
        # The right subtree will be constructed from elements in preorder[mid+1:] and inorder[mid+1:]
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        # Return the root of the constructed binary tree
        return root





class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Check if either the preorder or inorder list is empty
        if not preorder or not inorder:
            return None

        # Create a new TreeNode with the value of the first element in preorder
        root = TreeNode(preorder[0])

        # Find the index of the root value in the inorder list
        mid = inorder.index(preorder[0])

        # Recursively build the left subtree using elements in preorder and inorder before the root
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # Recursively build the right subtree using elements in preorder and inorder after the root
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # Return the root of the constructed tree
        return root

