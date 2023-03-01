# 147. Insertion Sort List
# Medium
# 2.5K
# 831
# Companies
# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

# The steps of the insertion sort algorithm:

# Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
# It repeats until no input elements remain.
# The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.


 

# Example 1:


# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5000].
# -5000 <= Node.val <= 5000
# Accepted
# 316.3K
# Submissions
# 622.2K
# Acceptance Rate
# 50.8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # create a dummy node to later refer to its next
        dummy = ListNode(0,head)
        # prev will be our head and curr will be head.next
        prev, curr = head,head.next
        # we can't go back so keep a previous pointer 
        
        # while we have a curr
        while curr:
            # if the current value is greater than or equal to the prev value
            # just update the prev to equal the curr, and the curr to equal curr.next
            # this means that this subportion is already sorted to continue
            if curr.val >= prev.val:
                prev = curr
                curr = curr.next
                continue
            # else, we set a temp variable to be our dummy
            # this is to help us iterate from the beginning of the linked list
            temp =  dummy
            # while curr.val is greater than the temp's next val,
            while curr.val > temp.next.val:
                # let our temp become temp.next ( move to the right)
                temp = temp.next
            # our prev's next is now curr.next
            prev.next = curr.next
            # our current's next becomes temp.next
            curr.next = temp.next
            # our temp's next equals curr
            temp.next = curr
            # curr becomes prev.next
            curr = prev.next
        # return dummy.next 
        return dummy.next
