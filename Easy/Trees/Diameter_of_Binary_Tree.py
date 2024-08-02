# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depthOfBinaryTree(self, root):

        if not root: return 0

        self.ans = max(self.ans, self.depthOfBinaryTree(root.left) + self.depthOfBinaryTree(root.right))

        return 1 + max(self.depthOfBinaryTree(root.left), self.depthOfBinaryTree(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        self.depthOfBinaryTree(root)

        return self.ans
        
