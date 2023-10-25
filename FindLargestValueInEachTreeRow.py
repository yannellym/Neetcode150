515. Find Largest Value in Each Tree Row
Solved
Medium
Topics
Companies
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
Accepted
308.3K
Submissions
470K
Acceptance Rate
65.6%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = [root] if root else None
        res = []


        while q:
            n = len(q)
            values = []
            for i in range(n):
                selected = q.pop(0)

                if selected.left:
                    q.append(selected.left)
                if selected.right:
                    q.append(selected.right)
                values.append(selected.val)
            res.append(max(values))
        return res
