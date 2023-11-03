Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.
 

Example 1:


Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.
Example 2:


Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
Accepted
112.2K
Submissions
128.9K
Acceptance Rate
87.0%
Seen this question in a real interview before?
1/4
Yes
No
Similar Questions
Discussion (53)

Choose a type







 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # Define a variable to count the nodes meeting the condition
        count = 0

        # Define a postorder traversal function
        def postorder(node):
            nonlocal count

            if not node:
                return (0, 0)

            # Recursively calculate the sum and count of nodes in the left and right subtrees
            left_sum, left_cnt = postorder(node.left)
            right_sum, right_cnt = postorder(node.right)

            # Calculate the sum and count of the current subtree
            cur_sum = node.val + left_sum + right_sum

            # number of nodes + 1 (to count the root node of the current tree) this gets us the length
            length = (left_cnt + right_cnt + 1)

            # Calculate the average of the current subtree, using integer division (//)
            # sum // length
            cur_avg = cur_sum // length

            # Check if the current node's value is equal to the calculated average
            if node.val == cur_avg:
                count += 1

            # Return the sum and count of nodes in the current subtree
            return (cur_sum, length)

        # Start the postorder traversal from the root node
        postorder(root)

        # Return the count of nodes that meet the condition
        return count










Copyright ©️ 2023 LeetCode All rights reserved
