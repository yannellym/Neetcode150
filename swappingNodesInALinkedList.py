# 1721. Swapping Nodes in a Linked List
# Medium
# 4.8K
# 160
# company
# Adobe
# company
# Amazon
# company
# Facebook
# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 105
# 0 <= Node.val <= 100
# Accepted
# 279K
# Submissions
# 405.6K
# Acceptance Rate
# 68.8%


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

      

        curr = head

        for i in range(k-1):
            curr = curr.next

        # save the left node
        left = curr
        right = head

        # starting at the left node, iterate until the end of the list
        while curr.next:
            # move curr
            curr = curr.next
            # move right (this node will land in length - k val)
            right = right.next
        
        left.val, right.val = right.val, left.val
        return head

