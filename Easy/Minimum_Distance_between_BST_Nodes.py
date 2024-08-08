# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def help(self, root):

        return self.help(root.left) + [root.val] + self.help(root.right) if root else []

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        mp = self.help(root)

        ans = math.inf

        for i in range(1, len(mp)):
            ans = min(ans, mp[i] - mp[i - 1])

        return ans
        
        
