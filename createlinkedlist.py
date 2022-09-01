# create linked list
# Write a function, create_linked_list, that takes in a list of values as an argument. The function should create a linked list containing each item of the list as the values of the nodes. The function should return the head of the linked list.

# test_00:
# create_linked_list(["h", "e", "y"])
# # h -> e -> y
# test_01:
# create_linked_list([1, 7, 1, 8])
# # 1 -> 7 -> 1 -> 8
# test_02:
# create_linked_list(["a"])
# # a
# test_03:
# create_linked_list([])
# # null

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
 
  head = Node(None)
  current = head
  for letter in values:
    current.next = Node(letter)
    current = current.next
  return head.next

    
