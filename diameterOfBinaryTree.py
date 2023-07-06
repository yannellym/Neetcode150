# 543. Diameter of Binary Tree
# Easy
# 11.8K
# 730
# company
# Amazon
# company
# Facebook
# company
# Bloomberg
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100
# Accepted
# 1.1M
# Submissions
# 1.9M
# Acceptance Rate
# 57.4%


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """


        max_diameter = [0]
        self.diameterOfBinaryTreeHelper(root, max_diameter)
        return max_diameter[0]


    def diameterOfBinaryTreeHelper(self, node, max_d):
        if node is None:
            return 0
        # Recursively calculate the heights of the left and right subtrees by calling the 
        # diameterOfBinaryTreeHelper function on the left and right children of the current node.
        left_height = self.diameterOfBinaryTreeHelper(node.left, max_d)
        right_height = self.diameterOfBinaryTreeHelper(node.right,max_d)

        # Calculate the diameter of the current node as the sum of the heights of the left and right subtrees.
        current_diameter = left_height + right_height
        # Update the maximum diameter seen so far by comparing it with the diameter of the current node.
        max_d[0] = max(max_d[0], current_diameter)
        # Return the height of the current node as the maximum height of the left and right subtrees plus 1.
        return max(left_height, right_height) + 1


        #The algorithm has a time complexity of O(N), where N is the number of nodes in the binary tree.
        # this algo basically starts bottoms up, then looks at each node and counts the length of the left and right sides and adds 1. This will set the height of each individual subtree. Then, it will calculate the current diameter as the sum of those two. Lastly, it updates the max diameter. 
    '''
    In the case of the max_diameter variable, we want to modify it within the diameterOfBinaryTreeHelper `function and keep track of the maximum diameter seen so far. If we simply declare max_diameter = 0 within the diameterOfBinaryTreeHelper function, any modifications made to max_diameter will create a new local variable instead of modifying the outer variable.

To overcome this limitation, we use a mutable object like a list, which can be modified within the nested function. By using max_diameter = [0], we create a list containing a single element with an initial value of 0. This list can be modified within the diameterOfBinaryTreeHelper function, and any changes made to it will be reflected outside the function.`
    '''
