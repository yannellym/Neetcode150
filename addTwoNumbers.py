# 2. Add Two Numbers
# Medium
# 24.3K
# 4.7K
# Companies
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # create a dummy node, a current, and carry variable
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        # while we have a list1 or a list 2 or a carry
        while l1 or l2 or carry:
            # select the val of list1 if we have one. If not, select 0
            v1 = l1.val if l1 else 0
            # select the val of list2 if we have one. If not, select 0
            v2 = l2.val if l2 else 0
            
            # add the value1 one and value1 together and the carry 
            val = v1 + v2 + carry
            # make sure to divide the carry by 10
            carry = val // 10
            # the value will be equal to value modulo 10
            val = val % 10
            # current.next will now equal a new node with that value
            cur.next = ListNode(val)
            
            # current will equal current.next
            cur = cur.next
            # if theres still a list1, assign list1.next to l1 if not None
            l1 = l1.next if l1 else None
            # if theres still a list2, assign list1.next to l1 if not None
            l2 = l2.next if l2 else None

        return dummy.next
