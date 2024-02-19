class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs = 0
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            if sums > 0:
                maxs = max(maxs,sums)
            else:
                sums = 0
        if max(nums) < 0:
            return max(nums)
        return maxs