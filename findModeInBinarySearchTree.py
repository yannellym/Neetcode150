501. Find Mode in Binary Search Tree
Solved
Easy
Topics
Companies
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
 

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
Accepted
253.6K
Submissions
470.8K
Acceptance Rate
53.9%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def in_order_traversal(node):
            nonlocal prev_val, max_count, count, modes

            if not node:
                return

            # Traverse the left subtree
            in_order_traversal(node.left)

            # Initialize prev_val if it's None
            if prev_val is None:
                prev_val = node.val

            # Check the current node's value
            if prev_val == node.val:
                count += 1
            else:
                count = 1
                prev_val = node.val

            # Update modes if the current count is greater than max_count
            if count > max_count:
                max_count = count
                modes = [node.val]
            elif count == max_count:
                modes.append(node.val)

            # Traverse the right subtree
            in_order_traversal(node.right)

        prev_val = None
        max_count = 0
        count = 0
        modes = []

        in_order_traversal(root)

        return modes


# or 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        

        def linearSearch(node):
            nonlocal maxcount, prevval, res, count
            if not node:
                return 

            linearSearch(node.left)

            if prevval is None:
                prevval = node.val
            
            if node.val == prevval:
                count += 1
            else:
                count = 1 
                prevval = node.val
            
            if count > maxcount:
                maxcount = count
                res = [node.val]
            elif count == maxcount:
                res.append(node.val)

            linearSearch(node.right)

        maxcount = 0
        count = 0
        prevval = None
        res = []

        linearSearch(root)
        return res
