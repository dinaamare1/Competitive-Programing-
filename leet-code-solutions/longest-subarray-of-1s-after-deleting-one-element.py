class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        l = 0
        maxs = float("-inf")
        for r in range(len(nums)):
            dic[nums[r]] += 1
            while dic[0] > 1:
                dic[nums[l]] -= 1
                l += 1
            maxs = max(maxs,r-l)
        return maxs