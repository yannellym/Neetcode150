# 61. Rotate List
# Medium
# 7.9K
# 1.4K
# company
# Amazon
# company
# LinkedIn
# company
# Bloomberg
# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109
# Accepted
# 735.2K
# Submissions
# 2M
# Acceptance Rate
# 36.3%


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        # have a pointer placed at the kth spot
        # move the slow pointer while fast

        # have slow.next = None
        # and fast.next = head


        
        if not head:
            return None

        # Count the length of the linked list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Adjust the rotation amount if it exceeds the length
        k = k % length

        if k == 0:
            return head

        # Connect the tail to the head to form a circular list
        tail.next = head

        # Traverse to the new tail position
        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        # Break the circular list at the new tail position
        new_head = new_tail.next
        new_tail.next = None

        return new_head
