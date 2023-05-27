# 876. Middle of the Linked List
# Easy

# 6772

# 179

# Add to List

# Share
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# fast and slow approach
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow = head
        fast = head
        prev = None

        # you advance fast by two steps until it is out of bounds
        while fast and fast.next:
            fast = fast.next.next

            # reverse half of the list 
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # return the last node we stopped on after reversing which will be the middle node
        return slow

# no need to reverse. Just the last slow node!
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next

            slow = slow.next
        return slow
