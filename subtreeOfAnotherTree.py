btr572. Subtree of Another Tree
Easy
7.6K
435
company
Amazon
company
Facebook
company
Microsoft
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
Accepted
697.8K
Submissions
1.5M
Acceptance Rate
46.8%
Seen this question in a real interview before?
1/4
Yes
No
Similar Questions
Related Topics


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def isSame(r, subR):
            if not r and not subR:
                return True
            if not r or not subR:
                return False
            if r.val != subR.val:
                return False
            # check the children
            return isSame(r.left, subR.left) and isSame(r.right, subR.right)

        if not root:
            return False
        # checks if the current root is the same as subRoot
        if isSame(root, subRoot):
            return True
        #  If not, it recursively calls itself on the left and right subtrees of the current root 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
