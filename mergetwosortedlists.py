# 21. Merge Two Sorted Lists
# Easy

# 15064

# 1323

# Add to List

# Share
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """   
         # create a dummy head
        dummy_head = ListNode()
        # have the current pointer point to the dummy head
        curr = dummy_head
        # make references for list1 and list 2
        head1 = list1
        head2 = list2
        # while we have list 2 and list2
        while head1 and head2:
            # if the value of the node at list1 is less than
            # the value of the node at list2
            if head1.val < head2.val:
                # have the curr.next equal list1 node
                curr.next = head1
                # the new list1 reference will be equal to its next
                head1 = head1.next
            else:
                # ehave the curr.next equal list2 node
                curr.next = head2
                # the new list2 reference will be equal to its next
                head2 = head2.next
            # move the curr to its next
            curr = curr.next
        # if we still have a head1, make curr.next the rest of head1
        if head1:
            curr.next = head1
        # if we still have a head2, make curr.next the rest of head2
        if head2:
            curr.next = head2
        # return dummy.next
        return dummy_head.next
       
