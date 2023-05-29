# 2130. Maximum Twin Sum of a Linked List
# Medium

# 1163

# 38

# Add to List

# Share
# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

# Example 1:


# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6. 
# Example 2:


# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
# Example 3:


# Input: head = [1,100000]
# Output: 100001
# Explanation:
# There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

# Constraints:

# The number of nodes in the list is an even integer in the range [2, 105].
# 1 <= Node.val <= 105

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



# SLOW AND FAST POINTER APPROACH
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        # our fast and slow pointers
        slow = head
        fast = head
        prev = None

        # find the halfway point of the list
        while fast and fast.next:
            fast = fast.next.next
            #reverse the first half 
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # slow will now be at the head of our second half
        # prev will now be the head of our reversed first half

        # var to get updated 
        maxCount = 0

        # while we have slow (the shorter list)
        while slow:
            # take the max
            maxCount = max(maxCount, slow.val + prev.val)
            # advance the pointers
            prev = prev.next
            slow = slow.next
        return maxCount
       
       
       
       
       
       
 # ARRAY SOLUTION 
       
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        values = []
        res = 0

        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next

        
        l = 0
        r = len(values)-1

        while l<=r:
            val = values[l] + values[r]
            res = max(res, val)
            l +=1
            r -=1
        return res
            


            
