988. Smallest String Starting From Leaf
Solved
Medium
Topics
Companies
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

 

Example 1:


Input: root = [0,1,2,3,4,3,4]
Output: "dba"
Example 2:


Input: root = [25,1,3,1,3,0,2]
Output: "adz"
Example 3:


Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def get_leaf_to_root_paths(root, path):
            if not root:
                return []

            # Append the current node's value to the path
            path.append(chr(root.val + ord('a')))  # Convert node value to character
            
            # If it's a leaf node, return the path from leaf to root
            if not root.left and not root.right:
                return [''.join(reversed(path))]  # Return the path in leaf-to-root order
            
            # Recursively traverse the left and right subtrees
            left_paths = get_leaf_to_root_paths(root.left, path[:])
            right_paths = get_leaf_to_root_paths(root.right, path[:])
            
            # Combine paths from left and right subtrees
            return left_paths + right_paths

        leaf_to_root_paths = get_leaf_to_root_paths(root, [])
        return min(leaf_to_root_paths) if leaf_to_root_paths else ""


        '''So, when you add root.val to ord('a'), you're effectively converting the numeric value stored in the node root into its corresponding lowercase letter. For example:

If root.val is 0, then root.val + ord('a') equals 97, which corresponds to 'a'.
If root.val is 1, then root.val + ord('a') equals 98, which corresponds to 'b'.
'''
