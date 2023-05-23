# 703. Kth Largest Element in a Stream
# Easy
# 4.5K
# 2.7K
# company
# Amazon
# company
# Facebook
# company
# Adobe
# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

# Example 1:

# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]

# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8

import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # declare self.k 
        self.k = k
        # create an empty heap
        self.heap = []
        # for every num in nums, call self.add and add it to the heap
        # this will insert in order AND MAINTAIN ONLY K in the heap
        for num in nums:
            self.add(num)
        # The heapify operation is not necessary in this case because we are initializing the heap by 
        # inserting elements one by one using heappush. 
        # The heappush function maintains the heap property as each element is inserted

    def add(self, val: int) -> int:
        # insert the val to the heap while mainting order by using heappush
        heapq.heappush(self.heap, val)
        # if the length of the heap is greater than k
        if len(self.heap) > self.k:
            # pop the smallest in the heap (top one)
            heapq.heappop(self.heap)
        # return the first one in the heap. 
        return self.heap[0]
