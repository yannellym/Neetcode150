# 113. Path Sum II
# Medium
# 6.7K
# 139
# Companies
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000



# Accepted
# 724.3K
# Submissions
# 1.3M
# Acceptance Rate
# 57.0%

 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
         # create a helpher function to do depth first search
        def dfs(node, path, curSum):
            # add the node value to our current sum
            curSum += node.val
            # add the path + our current node value and set tempPath to this result
            tempPath = path + [node.val]
            # if there's a node on the left, recursively call node.left,
            # pass in the tempPath list, and the current sum
            if node.left:
                dfs(node.left, tempPath, curSum)
            # if there's a node on the right, recursively call node.right,
            # pass in the tempPath list, and the current sum
            if node.right:
                dfs(node.right, tempPath, curSum)
            # if we are on a leaf node, and the current sum = the targetsum:
            # append the temporary path list to the result
            if not node.left and not node.right and curSum == targetSum:
                res.append(tempPath)

        # if there's not a root, return []
        if not root: return []
        # create a list for our answers
        res = []
        # call our helper dfs func and pass in the root, an empty list, and 0
        # these will signify our root, our list of paths, and our current sum
        dfs(root, [], 0)
        return res
            
