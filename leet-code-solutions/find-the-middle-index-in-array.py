class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_forward = [0]*(n+1)
        prefix_backward = [0]*(n+1)
        for i in range(n):
            prefix_forward[i+1] = prefix_forward[i] + nums[i]
        nums = nums[::-1]
        for i in range(n):
            prefix_backward[i+1] = prefix_backward[i] + nums[i]
        prefix_forward=prefix_forward[1:]
        prefix_backward=prefix_backward[1:][::-1]
        for i in range(n):
            if prefix_forward[i] == prefix_backward[i]:
                return i
        return -1
        
        
        
        