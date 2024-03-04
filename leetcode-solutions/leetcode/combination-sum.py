class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        bucket = []
        sums = 0
        def backtrack(idx):
            nonlocal sums
            if sums > target:
                return
            if sums == target:
                ans.append(bucket[:])
                return

            for i in range(idx,len(candidates)):
                bucket.append(candidates[i])
                sums += candidates[i]
                backtrack(i)
                sums -= candidates[i]
                bucket.pop()
                
        backtrack(0)
        return ans
