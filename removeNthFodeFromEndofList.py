# Remove Nth Node From End of List
# Medium
# 14.6K
# 607
# Companies
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# Follow up: Could you do this in one pass?

# Accepted
# 1.9M
# Submissions
# 4.7M
# Acceptance Rate
# 40.6%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # iterate through the whole list
        curr = head
        store = []

        while curr:
            # append the values to a store
            store.append(curr.val)
            # set curr to equal curr.next
            curr = curr.next
        # we are figuring out the index of the value we need
        # so we do the length of the store minus - n
        selected = len(store)-n

        # if the length of the store is 1, just return
        if len(store) == 1:
            return 

        prev = head
        curr = prev
        # a count to verify which index we are on
        count = 0
        # iterate through the entire list
        # have a prev, and current pointer
        while curr :
        # if the count(our index) is equal to selected(our target index)
            if count == selected:
                # if the current equals the previous, it must mean it is our first node
                if curr == prev:
                    # just return head.next!
                    return head.next
                else:
                    # else, have the previous equal the curr.next
                    prev.next = curr.next
                    # the curr = curr.next
                    curr = curr.next
                    # break out of the loop since we dont need to do anything else
                    break
            else:
                # else, just advance prev to the current
                prev = curr
                # the current will equal curr.next
                curr = curr.next
                # advance your count so it will equal the next index
                count += 1
        # return the modified list
        return head
