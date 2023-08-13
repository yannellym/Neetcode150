1448. Count Good Nodes in Binary Tree
Medium
5.2K
133
company
Microsoft
company
Google
company
Amazon
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
Accepted
356.2K
Submissions
483K
Acceptance Rate
73.8%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        

        def checkPath(node, max_value):
            if not node:
                return 0  # Base case: no nodes, so no contribution to count
            
            if node.val >= max_value:
                max_value = node.val  # Update max_value if current node's value is greater
                count = 1  # Increment count because current node is a good node
            else:
                count = 0  # Current node's value is not greater, so not a good node
            
            # Recursively check left and right subtrees, passing updated max_value
            count += checkPath(node.left, max_value)
            count += checkPath(node.right, max_value)
            
            return count  # Return the total count of good nodes
        
        return checkPath(root, float('-inf'))  # Start with negative infinity as initial max_value
