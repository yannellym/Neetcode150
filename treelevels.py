# tree levels
# Write a function, tree_levels, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each sublist represents a level of the tree.

# test_00:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

# tree_levels(a) # ->
# # [
# #   ['a'],
# #   ['b', 'c'],
# #   ['d', 'e', 'f']
# # ]
# test_01:
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# h = Node('h')
# i = Node('i')

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# e.right = h
# f.left = i

# #         a
# #      /    \
# #     b      c
# #   /  \      \
# #  d    e      f
# #      / \    /
# #     g  h   i

# tree_levels(a) # ->
# # [
# #   ['a'],
# #   ['b', 'c'],
# #   ['d', 'e', 'f'],
# #   ['g', 'h', 'i']
# # ]
# test_02:
# q = Node('q')
# r = Node('r')
# s = Node('s')
# t = Node('t')
# u = Node('u')
# v = Node('v')

# q.left = r
# q.right = s
# r.right = t
# t.left = u
# u.right = v

# #      q
# #    /   \
# #   r     s
# #    \
# #     t
# #    /
# #   u
# #  /
# # v

# tree_levels(q) # ->
# # [
# #   ['q'],
# #   ['r', 's'],
# #   ['t'],
# #   ['u'],
# #   ['v']
# # ]
# test_03:
# tree_levels(None) # -> []


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

breadth first (iterative)
from collections import deque
    
def tree_levels(root):
  if root is None:
    return []
  
  levels = []
  queue = deque([ (root, 0) ])
  while queue:
    current, level_num = queue.popleft()
    
    if len(levels) == level_num:
      levels.append([ current.val ])
    else:
      levels[level_num].append(current.val)
      
    if current.left is not None:
      queue.append((current.left, level_num + 1))
      
    if current.right is not None:
      queue.append((current.right, level_num + 1))
  
  return levels
n = number of nodes
Time: O(n)
Space: O(n)
