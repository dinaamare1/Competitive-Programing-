class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxs = float("-inf")
        zeros = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            while zeros>k:
                if nums[l] == 0:
                    zeros -= 1
                print(r-l)
                l+= 1
            maxs = max(maxs,r-l+1)
        return maxs
        