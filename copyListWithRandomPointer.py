# 138. Copy List with Random Pointer
# Medium
# 11.2K
# 1.2K
# company
# Amazon
# company
# Facebook
# company
# Bloomberg
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

 

# Example 1:


# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Example 2:


# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:



# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
 

# Constraints:

# 0 <= n <= 1000
# -104 <= Node.val <= 104
# Node.random is null or is pointing to some node in the linked list.
# Accepted
# 953.6K
# Submissions
# 1.8M
# Acceptance Rate
# 51.7


"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # create a hashmap that will have the following:
        # key = original node  , value = cocpy of node
        # include edge case where original node is none
        oldToCopy = {None: None}

        cur = head
        # iterate through the original list
        while cur:
            # make a copy of the current node
            copy = Node(cur.val)
            # add the curr node as the key and the copy as the value
            oldToCopy[cur] = copy
            # advance curr to the next
            cur = cur.next
        
        
        cur = head
        # iterate through the original list
        while cur:
            # get the copy of the curr node from the hashmap
            copy = oldToCopy[cur]
            # set the copy's next to be the curr's next copy
            copy.next = oldToCopy[cur.next]
            # set the copy's random to be the curr.random's copy
            copy.random = oldToCopy[cur.random]
            # advance curr to curr.next
            cur = cur.next
        # return the copy of the original head node in the hashmap
        return oldToCopy[head]
