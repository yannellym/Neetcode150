# 86. Partition List
# Medium
# 5.5K
# 629
# company
# Adobe
# company
# Google
# company
# Bloomberg
# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

 

# Example 1:


# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]
 

# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
# Accepted
# 453.1K
# Submissions
# 867.6K

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left = ListNode()
        right = ListNode()
        
        l = left
        r = right

        curr = head

        while curr:
            if curr.val < x :
                l.next = curr
                l = l.next
            else: 
                r.next = curr
                r = r.next
         
            curr = curr.next

        # need to advance the subnodes themselves not the heads
        r.next = None
        l.next = right.next
       
        
        return left.next

        


# Acceptance Rate
# 52.2%
# alternate 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # create a dummy node for list 1 and list 2
        list1 = ListNode()
        list2 = ListNode()
        # create two nodes that reference list1 and list2 and will move through our list
        ltail = list1
        rtail = list2

        # while we have a head value
        while head:
            # if the value of the head is less than x
            if head.val < x:
                # make the left's tail .next equal to head
                ltail.next = head
                # move left'tail to equal left's tail .next
                ltail = ltail.next
            else:
                # make right's tail.next = head
                rtail.next = head
                # right tail equals right tails ' .next
                rtail = rtail.next
            # move along the head to head.next
            head = head.next
        # connect the two lists
        ltail.next = list2.next
        # make sure you end list2 by assuring that rtail's .next is None
        rtail.next = None
        # return list1.next since list1 is a dummy node
        return list1.next
