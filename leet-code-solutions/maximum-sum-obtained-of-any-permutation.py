class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        requests.sort(key=lambda x:x[0])
        prefix = [0]*len(nums)
        for start,end in requests:
            prefix[start] += 1
            if end+1<len(nums):
                prefix[end+1] -= 1
        ans = []
        sums = 0
        for i in range(len(prefix)):
            sums += prefix[i]
            ans.append(sums)
        ans.sort(reverse=True)
        nums.sort(reverse=True)
        # print(ans,prefix)
        res = 0
        for i in range(len(nums)):
            res+=(nums[i] * ans[i])
        return res%((10**9)+7)


        