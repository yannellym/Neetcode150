# 148. Sort List
# Medium
# 9.8K
# 293
# company
# Yahoo
# company
# Amazon
# company
# Apple
# Given the head of a linked list, return the list after sorting it in ascending order.

 

# Example 1:


# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105
 

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

# Accepted
# 636.7K
# Submissions
# 1.1M
# Acceptance Rate
# 55.5%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if there's no head, or only a head, return the head
        if not head or not head.next:
            return head
        # get the mid of the list
        mid = self.get_mid(head)
        tmp = mid.next
        mid.next = None
        right = tmp
        # sort the left and the right by calling them recursively
        left, right = self.sortList(head), self.sortList(right)
        # merge the two halves and return 
        return self.merge_two_sorted(left, right)


    def merge_two_sorted(self, list1, list2):
        # create a dummy node
        dummy = ListNode()
        # our tail value will reference the dummy node and move us through the list
        tail = dummy
        # while we have list1 and list2
        while list1 and list2:
            # if the value of list1 is less than the value of list2
            if list1.val < list2.val:
                # the tails.next will equal list1
                tail.next = list1
                # move list1 along
                list1 = list1.next
            else:
                # the tails.next will equal list2
                tail.next = list2
                # move list2 along
                list2 = list2.next
            # move the tail along
            tail = tail.next

        # if you still have a remaining nodes after our while loop, add the list the tail's next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        # return the next of the dummy
        return dummy.next


    def get_mid(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
