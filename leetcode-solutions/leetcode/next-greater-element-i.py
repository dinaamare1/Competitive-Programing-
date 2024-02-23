class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {n:i for i,n in enumerate(nums1)}
        ans = [-1]*len(nums1)
        stack = []
        for idx,val in enumerate(nums2):
            while stack and val > stack[-1]:
                x = stack.pop()
                index = dic[x]
                ans[index] = val
            if val in dic:
                stack.append(val)
        return ans



        