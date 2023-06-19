# 92. Reverse Linked List II
# Medium
# 9.2K
# 417
# company
# Amazon
# Media.net
# company
# Microsoft
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
 

# Follow up: Could you do it in one pass?
# Accepted
# 638K
# Submissions
# 1.4M
# Acceptance Rate
# 45.5

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        dummy = ListNode(0, head)
        cur = dummy

        # Find the node before the sublist
        for _ in range(left - 1):
            cur = cur.next
        # the idea is to save the first half under a variable
        # dont set the .next of the first half to none as we will need it to refer to .next.next 
        firstHalf = cur
        print(firstHalf)

        # Reverse the sublist
        prev = None
        curr = cur.next
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Connect the reversed sublist to the remaining list
        # 1-> ->  5
        firstHalf.next.next = curr
        # 1-> 4 -> 3 -> 2 ->  5
        firstHalf.next = prev

        return dummy.next

        # 1- > None   None <- 2 <- 3 <- 4  5


        return dummy.next

      
# firstHalf.next.next = curr: This line connects the last node of the reversed sublist to the node immediately after the sublist. The firstHalf.next points to the last node of the original sublist before it was reversed. By setting firstHalf.next.next = curr, the next reference of the last node in the reversed sublist is updated to point to the node immediately after the sublist.

# firstHalf.next = prev: This line connects the node before the sublist to the first node of the reversed sublist. Initially, firstHalf.next points to the last node of the original sublist. By setting firstHalf.next = prev, the next reference of the node before the sublist is updated to point to the first node of the reversed sublist (prev).





# we basically iterate through the list and save curr as the first half . 
# then we reverse the list
# then we make the first's half.next.next = equal the curr of the reversed list
# then make firsthalf's.next = prev
# return the dummy's next
