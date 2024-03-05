class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [val for val in range(1,10)]
        ans = []
        bucket = []
        sums = 0
        def combine(idx):
            nonlocal sums
            if len(bucket) == k and sums == n:
                if bucket not in ans:
                    ans.append(bucket[:])
                    return
            for i in range(idx,len(nums)):
                sums += nums[i]
                bucket.append(nums[i])
                combine(i+1)
                bucket.pop()
                sums -= nums[i]
        combine(0)
        return ans

        