# 23. Merge k Sorted Lists
# Hard
# 17.4K
# 626
# company
# Google
# company
# Amazon
# company
# Tesla
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.
# Accepted
# 1.7M
# Submissions
# 3.3M
# Acceptance Rate
# 50.2%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        # for every list in the array, input the node in a min heap
        # pop the min
        # build a dummy list and return dummy.next


        store = []
        heapq.heapify(store)

        for single in lists:
            curr = single
            while curr:
                # O(n log m) time complexity
                heapq.heappush(store, curr.val)
                curr = curr.next
        #print(store)
        dummy = ListNode()
        curr = dummy
        
        for i in range(len(store)):
            #print(heapq.heappop(store))
            node = ListNode(heapq.heappop(store))
            curr.next = node
            curr = curr.next
        # O(n log n)

        # space complexity O(n)
        
        return dummy.next
            
# more fficient 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

 
        # the idea is to merge two lists at a time
        # step 1: while the len of lists is greater than 0, iterate in steps of 2
            # take each starter node of both lists, and call the mergeSort func on it
            # the merge func will return a sorted list and insert in the mergedLists array
             # [ [1,1,2,3,4,4,5], [2,6]]
            # lists will now equal the mergedlists array
        # step 2:
            # the while loop will iterate again 
            # we will do the same process and compare the heads of both lists in the array(thus combining them correctly)
        # return the head of list from the lists array

    
        if not lists or len(lists) == 0:
            return None

        # while we have pairs (lists len > 1)
        while len(lists) > 1:
            # to store our temporary merged lists
            mergedLists = []
            # we iterate in 2's in order to get every pair of nodes
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # it might just happen that the lists len is odd so we add an error handling
                l2 = lists[i+1] if (i+1) < len(lists) else None
                # call mergeSort on both lists
                mergedLists.append(self.mergeSort(l1, l2))
    
            lists = mergedLists
        return lists[0]

    def mergeSort(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next




