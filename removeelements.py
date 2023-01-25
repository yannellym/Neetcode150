# 203. Remove Linked List Elements
# Easy

# 5820

# 181

# Add to List

# Share
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

# Example 1:


# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
         # if the head is empty, return an empty list
        if head == []:
            return []
        
        # previous will equal None, an curr will equal head
        prev = None
        curr = head

        # iterate while curr is not none
        while curr is not None:
            # if the current nodes' value equals the value given
            if curr.val == val:
                # if there is a previous node
                if prev:
                    # have the previous node's next point to the current node's next
                    # this removes the current node
                    prev.next = curr.next
                # if there's no previous node
                else:
                    # have the head point to the current node's next 
                    head = curr.next
                # advance the current node to the its next node
                curr = curr.next
            # if the current node's val doesnt equal the give val
            else:
                # have the previous node point ot the current node
                prev = curr
                # have the current node point to its next node
                curr = curr.next
        return head
