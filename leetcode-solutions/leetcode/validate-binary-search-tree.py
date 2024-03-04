# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def check(root):
            nonlocal ans
            if not root:
                return ans
            check(root.left)
            ans.append(root.val)
            check(root.right)
        check(root)
        return ans == sorted(ans) and len(set(ans)) == len(ans)
        # def check(lefts,rights):
        #     if not lefts.left and not rights.right:
        #         return True
        #     elif not lefts and rights:
        #         return check(rights,rights)
        #     elif lefts and not rights:
        #         return check(lefts,lefts)
        #     if lefts.left and lefts.left.val < lefts.val and rights.right and rights.right.val > rights.val:
        #         check(lefts.left,rights.right)
        #         return True
        #     elif not lefts.left and rights.right and rights.right.val > rights.val:
        #         return True
        #     elif not rights.right and lefts.left and lefts.left.val < lefts.val:
        #         return True
        #     else:
        #         return False
        #     return check(lefts.left,rights.right)
        # return check(root,root)
        