class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxs = len(nums)-1
        curr = 0
        for i in range(len(nums)-1):
            curr = max(curr-1,nums[i])
            if curr <= 0:
                return False
        return True

        