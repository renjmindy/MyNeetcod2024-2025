# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self, root, data):

        if not root: return None
        if not root.left and not root.right: data.append(root.val)

        self.help(root.left, data)
        self.help(root.right, data)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        ans1, ans2 = list(), list()

        self.help(root1, ans1)
        self.help(root2, ans2)

        return ans1 == ans2
