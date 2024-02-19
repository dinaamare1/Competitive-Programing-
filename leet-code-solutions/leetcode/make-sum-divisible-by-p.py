class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        dic = Counter()
        sums = sum(nums)
        target = sums%p
        dic[target] = -1
        pre = 0
        ans = float("inf")
        if sums%p == 0:
            return 0
        for i,val in enumerate(nums):
            pre += val
            s = pre%p
            if s in dic:
                ans = min(ans,i-dic[s])
            dic[(s+target)%p] = i
        if ans==n:
            return -1
        return ans

        