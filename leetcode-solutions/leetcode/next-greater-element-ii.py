class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        n = len(nums)
        stack = []
        nums = nums * 2
        for idx,num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                val = stack.pop()
                ans[val % n] = num
            stack.append(idx)
        return ans