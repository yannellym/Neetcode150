# 116. Populating Next Right Pointers in Each Node
# Medium
# 8.3K
# 278
# Companies
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

 

# Example 1:


# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 212 - 1].
# -1000 <= Node.val <= 1000


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
    
        # start the Q with root if root else just empty queue
        Q = collections.deque([root] if root else [])
        # while there is a Q
        while Q:
            # take the length of the Q
            n = len(Q)
            # loop as many times as the length of the Q
            for i in range(n):
                # pop the first element in the Q and make it the curr
                cur = Q.popleft()
                # if i == 0: current's next will equal None
                if i==0:
                    cur.next = None
                else:
                    # else, current's next, will equal the previous
                    cur.next = prev
                # if the current has a right node, append it to the Q
                if cur.right:
                    Q.append(cur.right)
                # if the current has a left node, append it to the Q
                if cur.left:
                    Q.append(cur.left)
                # set the previous to equal the current
                prev = cur
        return root
