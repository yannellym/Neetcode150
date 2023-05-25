# https://leetcode.com/problems/add-two-numbers-ii/description/
  
#   445. Add Two Numbers II
# Medium
# 4.5K
# 245
# company
# Bloomberg
# company
# Amazon
# company
# Microsoft
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
# Example 2:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
# Example 3:

# Input: l1 = [0], l2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
 

# Follow up: Could you solve it without reversing the input lists?

# Accepted
# 368.3K
# Submissions
# 617.1K
# Acceptance Rate
# 59.7%

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
        # reverse the nodes
        # add the node while we have l1 or l2
        # create a node and assign its next to result and result = node
        # move the pointers
        # at the end if there are any carries left, create a node and assign 
        # nodes next to equal result and result t0 equal node

        # the nodes are reversed
        l1 = self.reverseNodes(l1)
        l2 = self.reverseNodes(l2)
        
        # var will keep track of our # of carries
        carry = 0
        # create var initially as None (this will serve as our tail None)
        # this will also serve as a temp var for the curr sum
        result = None

        # while we have l1 or l2 (dont need both as we will replace non node with 0)
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # get the sum with the previous carry
            total = val1 + val2 + carry
            # determine the new carry
            carry = total //10
            # create the new node with the ones place from the total
            node = ListNode(total % 10)

            # first iteration: (Node1) -> None
            # second iteration: result = (Node2) -> (Node1)(result) - > None
            node.next = result
            result = node

            # we have to check if we still have l1 left, if so
            if l1:
                # make l1 equal l1.next to advance to the next pointer
                l1 = l1.next
            # we have to check if we still have l2 left, if so
            if l2:
                # make l2 equal l2.next to advance to the next pointer
                l2 = l2.next
        # if we finished the sum and there's still a carry, 
        # we need to make sure we take care of it
        # we create a node, set its next to result so we can link it to the linked list
        # set the result to equal the node (basically updating the head of the linked list)
        if carry > 0:
            node = ListNode(carry)
            node.next = result
            result = node
        # since the head of the new linked list will be represented by result, we return result
        return result

    # helper function to reverse the nodes in a linked list
    def reverseNodes(self, node):
        # sets a prev of None
        prev = None
        # curr will equal the head
        curr = node
        # while theres a curr (a node in the list)
        while curr:
            # store curr's next in a temp so we can refer to it later
            temp = curr.next 
            # set curr's next to equal prev so we reverse the link
            curr.next = prev
            # now prev will equal curr to we can update the node we're looking at
            prev = curr
            # curr will equal temp so we keep moving along the linked list for other nodes
            curr = temp
        # we return the prev because that's going to be the last node we visit in our
        # original linked lisit. 
        return prev
