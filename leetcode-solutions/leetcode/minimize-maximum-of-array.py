class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        sums = nums[0]
        for i in range(1,len(nums)):
            sums += nums[i]
            res = max(res,ceil(sums/(i+1)))
        return res
            
        