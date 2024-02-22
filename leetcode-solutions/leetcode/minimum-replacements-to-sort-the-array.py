class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        if sorted(nums) == nums:
            return 0
        else:
            nums = nums[::-1]
            maxs = nums[0]
            for i in range(1,len(nums)):
                k = ceil(nums[i]/maxs)
                ans += k-1
                maxs = nums[i]//k
            return ans



        