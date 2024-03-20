https://leetcode.com/problems/merge-in-between-linked-lists/?envType=daily-question&envId=2024-03-20

1669. Merge In Between Linked Lists
Solved
Medium
Topics
Companies
Hint
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:


Build the result list and return its head.

 

Example 1:


Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
Example 2:


Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.
 

Constraints:

3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104
Seen this question in a real interview before?
1/4
Yes
No
Accepted
88.8K
Submissions
122.1K
Acceptance Rate
72.7%



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        
        head1 = list1
        curr1 = head1
        head2 = list2

        for i in range(a-1):
            curr1 = curr1.next
        
        #nextone is now a+1 to end
        nextone = curr1.next
        curr1.next = None
        # head1 is now from 0 to a
        finalhead = head1
        # print(nextone)

        for i in range(b-a+1):
            nextone = nextone.next
        # this tail is now b+1 to end
        finaltail = nextone
        
        curr1.next = list2

        while curr1.next:
            curr1 = curr1.next
        # curr1 is now 0 to a plus list2
        # connect the end of list2 to the finaltil
        curr1.next = finaltail
        # return the new built list
        return finalhead

  
