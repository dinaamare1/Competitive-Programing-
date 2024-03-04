class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        bucket = []
        def combine(i):
            if len(bucket) == k:
                ans.append(bucket[:])
                return
            for i in range(i,n+1):
                bucket.append(i)
                combine(i+1)
                bucket.pop()
        combine(1)
        return ans
        