class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]*(n+1)
        ans = 0
        dic = defaultdict(int)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        for val in prefix:
            new = val+k
            ans += dic[val]
            dic[new] += 1
        return ans