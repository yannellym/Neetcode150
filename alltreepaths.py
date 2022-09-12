# all tree paths
# Write a function, all_tree_paths, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.

# The order within an individual path must start at the root and end at the leaf, but the relative order among paths in the outer list does not matter.

# You may assume that the input tree is non-empty.

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

# all_tree_paths(a) # ->
# # [ 
# #   [ 'a', 'b', 'd' ], 
# #   [ 'a', 'b', 'e' ], 
# #   [ 'a', 'c', 'f' ] 
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

# all_tree_paths(a) # ->
# # [ 
# #   [ 'a', 'b', 'd' ], 
# #   [ 'a', 'b', 'e', 'g' ], 
# #   [ 'a', 'b', 'e', 'h' ], 
# #   [ 'a', 'c', 'f', 'i' ] 
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

# all_tree_paths(q) # ->
# # [ 
# #   [ 'q', 'r', 't', 'u', 'v' ], 
# #   [ 'q', 's' ] 
# # ] 
# test_03:
# z = Node('z')

# #      z

# all_tree_paths(z) # -> 
# # [
# #   ['z']
# # ]

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):
  if not root:
    return []
  if not root.left and not root.right:
    return [ [root.val] ]
  
  all_paths = []
  
  left_path = all_tree_paths(root.left)
  for sub_path in left_path:
    all_paths.append([root.val, *sub_path])
    
  right_path = all_tree_paths(root.right)
  for sub_path in right_path:
    all_paths.append([root.val, *sub_path])
  
  return all_paths

