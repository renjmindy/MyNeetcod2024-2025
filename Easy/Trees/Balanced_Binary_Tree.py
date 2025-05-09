# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depthOfBinaryTree(self, root):

        if not root: return 0

        return 1 + max(self.depthOfBinaryTree(root.left), self.depthOfBinaryTree(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root: return True

        return abs(self.depthOfBinaryTree(root.left) - self.depthOfBinaryTree(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
