# 450. Delete Node in a BST
# Medium
# 7K
# 178
# Companies
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:

# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# Example 3:

# Input: root = [], key = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -105 <= Node.val <= 105
# Each node has a unique value.
# root is a valid binary search tree.
# -105 <= key <= 105
 

# Follow up: Could you solve it with time complexity O(height of tree)?

# Accepted
# 342.9K
# Submissions
# 682.6K
# Acceptance Rate
# 50.2%

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        '''
        If the key is greater than the value of the current root, 
        we need to search for the node to be deleted in the right subtree. 
        We do this by recursively calling the deleteNode function with the 
        current root's right child as the new root argument
        '''
        if key > root.val:
            root.right= self.deleteNode(root.right, key)
            '''
            If the key is less than the value of the current root, we need to 
            search for the node to be deleted in the left subtree. We do this by 
            recursively calling the deleteNode function with the current root's 
            left child as the new root argument.
            '''
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            '''
            If we reach this point, it means that we have found the node 
            to be deleted and need to perform the deletion. We check if the 
            current root has only one child (either left or right), in which
            case we simply return the non-None child to replace the root.
            '''
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
                '''
                If the root has two children, we need to find the minimum value in its 
                right subtree (which will be the leftmost child of its right subtree),
                and replace the root's value with that value. Then, we recursively call
                the deleteNode function with the root's right child and the value we just 
                replaced as the new key argument. This effectively removes the node with 
                that value from the right subtree and replaces the root's value with it.
                '''
            curr = root.right
            while curr.left:
               curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)
        '''
        Finally, we return the root to the caller of the function. This is necessary 
        because we may have modified the root during the deletion process, and need to 
        return the new root to the parent of the current root in the call stack.
        '''
        return root

        # https://www.youtube.com/watch?v=LFzAoJJt92M&ab_channel=NeetCodeIO
        # https://www.youtube.com/watch?v=wMyWHO9F1OM&ab_channel=TimothyHChang

# The function takes two arguments, root which represents the root of the current subtree, and key which is the value of the node to be deleted.
