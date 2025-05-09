# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], maxVal = math.inf, minVal = -math.inf) -> bool:
        
        if not root: return True
        elif root.val >= maxVal or root.val <= minVal: return False
        else: return self.isValidBST(root.left, root.val, minVal) and self.isValidBST(root.right, maxVal, root.val)
