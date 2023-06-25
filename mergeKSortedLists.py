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
            





