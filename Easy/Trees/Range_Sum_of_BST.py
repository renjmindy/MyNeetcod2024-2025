# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self, root, low, high):

        if not root: return None
        self.help(root.left, low, high)
        if root.val >= low and root.val <= high:
            self.ans.append(root.val)
        self.help(root.right, low, high)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.ans = list()

        self.help(root, low, high)

        return sum(self.ans)
