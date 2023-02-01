# Easy
# 5.6K
# 236
# Companies
# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:


# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105
# Accepted
# 436.1K
# Submissions
# 714.6K
# Acceptance Rate
# 61.0%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # store all values we have seen in a set (can save space for repeated vals)
        store = set()
        # helper func to traverse the tree by depth first search
        def dfs(node):
            # if there's no node:
            # return False
            if not node:
                return False
            # get the difference of the k and node.val and save it in diff variable
            diff = k - node.val
            # if diff is in the store, it means we can return true
            if diff in store:
                return True
            else:
                # if it is not in store, add it
                store.add(node.val)
            # recursively call dfs on left and right. 
            # only one has to return true in this case
            return (dfs(node.left) or dfs(node.right))
        # call dfs on root
        return dfs(root)

        
