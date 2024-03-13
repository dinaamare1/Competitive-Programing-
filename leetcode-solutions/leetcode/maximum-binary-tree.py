# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        

        def create(nums):
            if not nums:
                return                
            maxs = [float("-inf"),float("-inf")]
            for idx,val in enumerate(nums):
                if val>maxs[0]:
                    maxs[0] = val
                    maxs[1] = idx 
            root = TreeNode(maxs[0])
            root.left = create(nums[:maxs[1]])
            root.right = create(nums[maxs[1]+1:])
            return root
            
        return create(nums)
        