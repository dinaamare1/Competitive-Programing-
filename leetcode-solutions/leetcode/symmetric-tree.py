# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(lefts,rights):
            if not lefts and not rights:
                return True
            if lefts and not rights or rights and not lefts :
                return False
            else:
                return lefts.val == rights.val and check(lefts.right,rights.left) and check(lefts.left,rights.right)
        return check(root.left,root.right)