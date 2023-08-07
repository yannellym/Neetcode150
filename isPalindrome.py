Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in l, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers, determine whether or not it's a palindrome.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

Example

For l = [0, 1, 0], the output should be
solution(l) = true;

For l = [1, 2, 2, 3], the output should be
solution(l) = false.

Input/Output

[execution time limit] 4 seconds (py)

[memory limit] 1 GB

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 5 · 105,
-109 ≤ element value ≤ 109.

[output] boolean

Return true if l is a palindrome, otherwise return false.

[Python 2] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print "This prints to the console when you Run Tests"
    return "Hello, " + name

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l):
    fast = l
    slow = l
    prev = None
    
    while fast and fast.next:
        
        fast = fast.next.next
        
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    
    
    if fast:
        slow = slow.next
    
        
    while prev and slow:
        if prev.value != slow.value:
            return False
        slow = slow.next
        prev = prev.next
    return True

#[1, 2, {3}, 1, 2, 3]

