2487. Remove Nodes From Linked List
Solved
Medium
Topics
Companies
Hint
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
Seen this question in a real interview before?
1/5
Yes
No
Accepted
167.6K
Submissions
225.6K
Acceptance Rate
74.3%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
  
        
        def reverseLinkedList(self, head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        def removeNodes(self, head):
            """
            :type head: Optional[ListNode]
            :rtype: Optional[ListNode]
            """
            head = self.reverseLinkedList(head)
            
            dummy = ListNode(0)
            dummy.next = head
            prev = dummy
            curr = head
            max_val = float('-inf')  # Initialize max_val to negative infinity

            # Traverse the reversed list
            while curr:
                # If current node's value is less than max_val, keep the node
                if curr.val < max_val:
                    prev.next = curr.next
                else:
                    # Update max_val with the maximum value seen so far
                    max_val = curr.val
                    # Move prev to the current node
                    prev = curr
                # Move to the next node
                curr = curr.next
            
            # Reverse the modified linked list back to its original order
            return self.reverseLinkedList(dummy.next)

        
