# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 
  
  # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        prev = None

        # finding the middle and reversing it
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # Adjust pointers for odd-length lists
        if fast:
            slow = slow.next

        # Compare the reversed first half with the second half
        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next

        return True
#I have added an adjustment for odd-length lists by moving the slow pointer forward by one position. This ensures that the middle element, which does not need to be checked for palindromes, is skipped.

# With the given input of [1, 0, 1], the corrected code will now correctly output True, indicating that the linked list is a palindrome.
