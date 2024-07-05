
Code
Submissions
Submissions
Testcase
Testcase
Test Result
Test Result
Accepted
2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
Solved
Medium
Topics
Companies
Hint
A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

 

Example 1:


Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].
Example 2:


Input: head = [5,3,1,2,5,1,2]
Output: [1,3]
Explanation: There are three critical points:
- [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.
Example 3:


Input: head = [1,3,2,2,3,2,2,2,7]
Output: [3,3]
Explanation: There are two critical points:
- [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        # Ensure there are at least three nodes to have critical points
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        # List to store the indices of critical points
        critical_points = []
        # Initialize the index for the current node
        index = 1
        # Pointers to the previous, current, and next nodes
        prev, curr, next = head, head.next, head.next.next

        # Traverse the linked list
        while next:
            # Check if the current node is a critical point
            if (curr.val > prev.val and curr.val > next.val) or (curr.val < prev.val and curr.val < next.val):
                critical_points.append(index)
            # Move the pointers to the next set of nodes
            prev, curr, next = curr, next, next.next
            # Increment the index
            index += 1

        # If there are fewer than two critical points, return [-1, -1]
        if len(critical_points) < 2:
            return [-1, -1]

        # Calculate the minimum distance between consecutive critical points
        # they could be any two points just not the same indexes
        min_distance = float('inf')
        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])

        # Calculate the maximum distance between the first and last critical points
        max_distance = critical_points[-1] - critical_points[0]

        # Return the results as a list [min_distance, max_distance]
        return [min_distance, max_distance]
