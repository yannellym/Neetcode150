https://leetcode.com/problems/construct-string-from-binary-tree/submissions/1061807559/
606. Construct String from Binary Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

 

Example 1:


Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
Example 2:


Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-1000 <= Node.val <= 1000
Accepted
227.8K
Submissions
352.3K
Acceptance Rate
64.7%
\\
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""  # If the node is None, return an empty string
    
        result = str(root.val)  # Convert the current node's value to a string and start building the result string
        
        if root.left or root.right:
            # If the node has a left or right child, include an opening parenthesis and the string representation of the left subtree
            # if ewe have a node that has a right child but no left child, add an empty parenthesis.
            result += "(" + self.tree2str(root.left) + ")"
        
        if root.right:
            # If the node has a right child, include an opening parenthesis and the string representation of the right subtree
            result += "(" + self.tree2str(root.right) + ")"
        
        return result
