Note: Try to solve this task in O(list size) time using O(1) additional space, since this is what you'll be asked during an interview.

Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.

Example

For l = [1, 2, 3, 4, 5] and n = 3, the output should be
solution(l, n) = [3, 4, 5, 1, 2];
For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
solution(l, n) = [7, 1, 2, 3, 4, 5, 6].
Input/Output

[execution time limit] 4 seconds (py)

[memory limit] 1 GB

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 105,
-1000 ≤ element value ≤ 1000.

[input] integer n

A non-negative integer.

Guaranteed constraints:
0 ≤ n ≤ list size.

[output] linkedlist.integer

Return l with the n last elements moved to the beginning.

[Python 2] Syntax Tips

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, n):
    if n == 0 or not l or not l.next:
        return l
    
    length = 1
    current = l
    while current.next:
        length += 1
        current = current.next
    
    if n >= length:
        return l
    
    new_head_position = length - n
    
    current = l
    for _ in range(new_head_position - 1):
        current = current.next
    
    new_head = current.next
    current.next = None
    
    current = new_head
    while current.next:
        current = current.next
    current.next = l
    
    return new_head
