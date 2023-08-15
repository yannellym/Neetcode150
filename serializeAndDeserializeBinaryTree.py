# 297. Serialize and Deserialize Binary Tree
# Hard
# 9.4K
# 342
# company
# Amazon
# company
# Yahoo
# company
# Tesla
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

# Example 1:


# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000
# Accepted
# 771.4K
# Submissions
# 1.4M
# Acceptance Rate
# 55.8%


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):

        def dfs(node):
            if not node:
                return "X"  # Represent null nodes with "X"
            # Pre-order traversal: node value, left subtree, right subtree
            return str(node.val) + "," + dfs(node.left) + "," + dfs(node.right)
        # we do a preorder traversal and it will return this -> "1,2,X,X,3,4,X,X,5,X,X""
        return dfs(root)
    
    def deserialize(self, data):

        def buildTree(vals):
            if not vals:  # Check if the list is empty
              return None
            val = vals.pop(0)  # Pop the next value from the list
            if val == "X":
                return None  # Return None for null nodes

            node = TreeNode(int(val))
            
            # Recursively build left and right subtrees
            node.left = buildTree(vals)
            node.right = buildTree(vals)
            return node
        
        vals = data.split(',')  # Split serialized data by comma, now we have -> [1,2,X,X,3,4,X,X,5,X,X]
        return buildTree(vals)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
