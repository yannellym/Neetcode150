# longest streak
# Write a function, longest_streak, that takes in the head of a linked list as an argument. The function should return the length of the longest consecutive streak of the same value within the list.

# test_00:
# a = Node(5)
# b = Node(5)
# c = Node(7)
# d = Node(7)
# e = Node(7)
# f = Node(6)

# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f

# # 5 -> 5 -> 7 -> 7 -> 7 -> 6

# longest_streak(a) # 3
# test_01:
# a = Node(3)
# b = Node(3)
# c = Node(3)
# d = Node(3)
# e = Node(9)
# f = Node(9)

# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f

# # 3 -> 3 -> 3 -> 3 -> 9 -> 9

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):
  current = head
  max = 0
  counter = 0
  prev = None
  while current is not None: 
    if current.val == prev:
      counter += 1
    else:
      counter = 1
    prev = current.val
    
    if counter > max:
      max = counter
    
    current = current.next
      
  return max

# longest_streak(a) # 4
# test_02:
# a = Node(9)
# b = Node(9)
# c = Node(1)
# d = Node(9)
# e = Node(9)
# f = Node(9)

# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f

# # 9 -> 9 -> 1 -> 9 -> 9 -> 9

# longest_streak(a) # 3
# test_03:
# a = Node(5)
# b = Node(5)

# a.next = b

# # 5 -> 5

# longest_streak(a) # 2
# test_04:
# a = Node(4)

# # 4

# longest_streak(a) # 1
# test_05:
# longest_streak(None) # 0
