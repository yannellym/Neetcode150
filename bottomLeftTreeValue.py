513. Find Bottom Left Tree Value
Solved
Medium
Topics
Companies
Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # if root is None:
        #     return -1  # indicating an empty tree
        
        # q = [root]
        # leftmost_value = None

        # while q:
        #     level_size = len(q)
        #     leftmost_value = q[0].val  # updating leftmost_value at the start of each level

        #     for _ in range(level_size):
        #         node = q.pop(0)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)

        # return leftmost_value


        q = deque([root])
        while q:
            node = q.popleft()
            print(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            # print(node.val)
            ans = node.val
        return ans
        # we're adding the right now value first so rows are going right to left
        # last value is the leftmost value
