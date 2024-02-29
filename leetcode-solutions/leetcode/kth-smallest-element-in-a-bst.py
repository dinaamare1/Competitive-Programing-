# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def find(root):
            if root:
                find(root.left)
                ans.append(root.val)
                find(root.right)
            return ans
        return find(root)[k-1]

        