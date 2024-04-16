https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=daily-question&envId=2024-04-15


129. Sum Root to Leaf Numbers
Solved
Medium
Topics
Companies
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

 

Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
855K
Submissions
1.3M
Acceptance Rate
65.6%


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, path_sum):
            if not node:
                return 0
            # Calculate the sum formed by the path from root to current node
            path_sum = path_sum * 10 + node.val  # Multiply by 10 to shift the digits to the left
            # If it's a leaf node, return the path_sum
            if not node.left and not node.right:
                return path_sum
            # Recursively calculate the sum for left and right subtrees
            return dfs(node.left, path_sum) + dfs(node.right, path_sum)
        
        return dfs(root, 0)

        
