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
       # In the case where k is equal to the length of the list, the loop does not execute,
        #  and the new tail remains at the head of the list.
        if k == 0:
            return head

        # Traverse to the new tail position
        steps = length - k
        new_tail = head
        # steps -1 because we are already in the first position.
        for _ in range(steps - 1):
            new_tail = new_tail.next

        # save new_tail.next since itll be the new head
        # 1 -> 2 -> 3 ->    new_head 4 -> 5 ->
        new_head = new_tail.next
        # cut the first list :  1 -> 2 -> 3 -> None
        # end the first list by setting it's next to None
        new_tail.next = None
        # set the next pointer of the original tail. to be equal to the head.
        # new_head 4 -> 5 -> 1 -> 2 -> 3 -> None
        tail.next = head

        return new_head
