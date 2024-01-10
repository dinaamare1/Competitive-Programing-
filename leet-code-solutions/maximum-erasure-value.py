class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        l = 0
        maxs = 0
        sums = 0
        for r in range(len(nums)):
            sums += nums[r]
            dic[nums[r]] += 1
            while dic[nums[r]] > 1:
                sums -= nums[l]
                dic[nums[l]] -= 1
                l += 1
            maxs = max(maxs,sums)
        return maxs
        