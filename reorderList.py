# 143. Reorder List
# Medium
# 8.8K
# 297
# company
# Amazon
# company
# Adobe
# company
# Google
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000
# Accepted
# 673.5K
# Submissions
# 1.3M
# Acceptance Rate
# 53.0%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
    
        # find the middle
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # set a new list for the second half of the arr
        second = slow.next
        # end the first list 
        slow.next = None

        # reverse second half list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # prev will now equal the head of the reversed second half
        
        # merge the two halves
        # after iterating through the second half of the list, prev will equal the
        # last node we visited (the head of the reversed linked list)
        first = head
        second = prev
        # second half could be shorter if its uneven
        while second:
            firsttemp = first.next
            secondtemp = second.next
            first.next = second
            second.next = firsttemp
            first = firsttemp
            second = secondtemp



            
