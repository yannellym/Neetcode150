# 701. Insert into a Binary Search Tree
# Medium
# 4.5K
# 156
# Companies
# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

# Example 1:


# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:

# Example 2:

# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]
# Example 3:

# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]
 

# Constraints:

# The number of nodes in the tree will be in the range [0, 104].
# -108 <= Node.val <= 108
# All the values Node.val are unique.
# -108 <= val <= 108
# It's guaranteed that val does not exist in the original BST.
# Accepted
# 384.1K
# Submissions
# 516K
# Acceptance Rate
# 74.4%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive method

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)  # Create a new node and return it as the root of the tree

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)  # Insert in the left subtree recursively
        else:
            root.right = self.insertIntoBST(root.right, val)  # Insert in the right subtree recursively
        
        return root

        '''
        In both cases, the recursive call effectively traverses down the tree until it finds the
         appropriate position to insert the new node. The recursion continues until it reaches a
          None node (end of a branch), at which point it creates a new node with the value val 
          and returns it. The returned node is then assigned as the new child of the root node, 
          effectively inserting the new node into the tree.
        '''





class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if there is no root, return a node with val inside
        if not root:
            return TreeNode(val)
        # helper function to insert
        def insert(node):
            # if the val is greater than the current node's value
            if val > node.val:
                # if there is no node in the right
                if not node.right:
                    # insert a new node to the right
                    node.right = TreeNode(val)
                else:
                    # if there is a node node to the right, call insert func again w/ node.right
                    insert(node.right)
            else:
                # if there is no node in the left
                if not node.left:
                    # insert a new node to the left
                    node.left = TreeNode(val)
                else:
                    # if there is a node node to the left, call insert func again w/ node.left
                    insert(node.left)
        #call helper function insert with the root as a value
        insert(root)
        # return the root as we want the entire tree
        return root

        # the key to solving this problem is knowing that you can insert it at the bottom of the leaf node.
