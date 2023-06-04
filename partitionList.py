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
        list1 = []
        list2 = []
        curr = head

        while curr:
            if curr.val < x:
                list1.append(curr.val)
            else:
                list2.append(curr.val)
            curr = curr.next
        
        dummy = ListNode(0)
        curr = dummy

        for i in range(len(list1)):
            curr.next = ListNode(list1[i])
            curr = curr.next
        
        for i in range(len(list2)):
            curr.next = ListNode(list2[i])
            curr = curr.next
        return dummy.next
        


# Acceptance Rate
# 52.2%
