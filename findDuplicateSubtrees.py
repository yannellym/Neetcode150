# 652. Find Duplicate Subtrees
# Medium
# 5K
# 404
# Companies
# Given the root of a binary tree, return all duplicate subtrees.

# For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with the same node values.

 

# Example 1:


# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
# Example 2:


# Input: root = [2,1,1]
# Output: [[1]]
# Example 3:


# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
 

# Constraints:

# The number of the nodes in the tree will be in the range [1, 5000]
# -200 <= Node.val <= 200

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        seen = defaultdict(int)
        dup = []
        
        def find(root):
            # if a node is None, return null
            if root is None:    
                return "Null"                             
            
            # call find on the root left and root right
            l = find(root.left)
            r = find(root.right)
            # create a string where the root val the left and the right are concatenated by
            # a period. They will help us distinguish the values
            # e.g. 1, 11 or 11, 1
            k = str(root.val) + "." + l + "." + r + "." 
            # if we have seen this string before, add one to it
            # first initialize din default dict is 0, then second iteration is 1, third is 2 

            seen[k] += 1
            # if we have seen this string twice(meaning two subtrees)
            if seen[k] == 2:
                # append this root to duplicates
                dup.append(root)
            
            return k # return key to save to seen
        
        find(root)
        return dup
