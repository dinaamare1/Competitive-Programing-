# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # self.dic = defaultdict(int)
        ans = []
        dic = defaultdict(int)
        def modes(root):
            if not root:
                return 
            if root.val in dic:
                dic[root.val] += 1
            else:
                dic[root.val] = 1
            modes(root.left)
            modes(root.right)
        modes(root)

        for key in dic:
            if dic[key] == max(dic.values()):
                ans.append(key)
        return ans

        