# 958. Check Completeness of a Binary Tree
# Medium
# 3.7K
# 48
# Companies
# Given the root of a binary tree, determine if it is a complete binary tree.

# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
# Example 2:


# Input: root = [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# 1 <= Node.val <= 1000
# Accepted
# 188.6K
# Submissions
# 336.4K
# Acceptance Rate
# 56.1%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Check if the root node is None, if so, return True (an empty tree is complete)
        if not root:
            return True

        # Create a deque to store the nodes of the tree in level order
        q = deque([root])

        # Traverse the tree in level order
        while q:
            # Remove the first node from the deque
            node = q.popleft()

            if node:
            # Add the left and right child nodes of the current node to the deque
                q.append(node.left)
                q.append(node.right)
            else:
                # if theres no node
                # while there's a q
                while q: 
                    # if you pop from the left and there is a value other than NONE, return false
                    # this means that it is not complete because we're supposed to have all NONE Values
                    if q.popleft():
                        return False
        # if we get here is because the code went into the else statement and while there was a q:
        # it kept poppin from it. It found all none values. Meaning our tree was complete.
        # then, it went to the top of the code again and saw that it couldnt execute "while q" 
        # and it came down here to return true
        return True


        # https://www.youtube.com/watch?v=olbiZ-EOSig&ab_channel=NeetCodeIO
