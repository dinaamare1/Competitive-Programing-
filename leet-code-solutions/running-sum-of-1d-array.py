class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0]*(len(nums)+1)
        # for i in range(len(nums) - 1):
        #     nums[i + 1] += nums[i]
        # return nums
        for i in range(len(nums)):
            ans[i+1] = ans[i]+nums[i]
        return ans[1:]