# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# Accepted
# 907.8K
# Submissions
# 1.5M
# Acceptance Rate
# 61.5%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        queue = collections.deque([root])

        result = []
        
        while queue:
            # get size of current level
            size = len(queue)
            # this is to track the last node we've seen
            rightValue = None
            # pop all nodes on this level
            for _ in range(size):
                current = queue.popleft()
                
                # need to add the children of all nodes on this level
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
                    
                # set this to be last
                rightValue = current
                
            # prev will hold the very last node on this level; hence, the "right"
            result.append(rightValue.val)
        
        return result
    # this algorithm works by getting the length of the Q, iterating nth times with n being the length of the Q.
    # every iteration, pop from the left and save that node in a "current" vatiable
    # if the node has a left, add it to the Q
    # if the node has a right, add it to the Q
    # set the rightValue var to equal the current
    # at the end of each level iteration, we will have the rightmost value in the var 
    # at the rightmost var's value to the result
    # return the result
