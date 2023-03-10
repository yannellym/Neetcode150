# 382. Linked List Random Node
# Medium
# 2.8K
# 654
# Companies
# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

# Implement the Solution class:

# Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
# int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.
 

# Example 1:


# Input
# ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
# [[[1, 2, 3]], [], [], [], [], []]
# Output
# [null, 1, 3, 2, 2, 3]

# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.getRandom(); // return 1
# solution.getRandom(); // return 3
# solution.getRandom(); // return 2
# solution.getRandom(); // return 2
# solution.getRandom(); // return 3
# // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
 

# Constraints:

# The number of nodes in the linked list will be in the range [1, 104].
# -104 <= Node.val <= 104
# At most 104 calls will be made to getRandom.
 

# Follow up:

# What if the linked list is extremely large and its length is unknown to you?
# Could you solve this efficiently without using extra space?
# Accepted
# 215.2K
# Submissions
# 344.2K
# Acceptance Rate
# 62.5%
import random

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

   
    def __init__(self, head):
        # initiate our list
        self.nodes = []
        # iterate through all the nodes and add the value of the node to the list
        while head:
            self.nodes.append(head.val)
            # dont forget to point to the next node
            head = head.next

    def getRandom(self):
        # create an i variable(for index) and set a random number starting at 0 and ending at length 
        # of our nodes list - 1
        # this will ensure all of our nodes have an equal probability of getting chosen
        i = random.randint(0, len(self.nodes) - 1)
        # return a node in our nodes list 
        return self.nodes[i]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
