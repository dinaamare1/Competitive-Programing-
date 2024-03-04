class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        bucket = []
        sums = 0
        visted = set()
        candidates.sort()
        def backtrack(idx):
            nonlocal sums
            if sums > target or idx>len(candidates):
                return
            if sums == target:
                if bucket not in ans:
                    ans.append(bucket[:])
                    return
                # if tuple(bucket[:]) not in visted:
                #     visted.add(tuple(bucket[:]))
                #     return
            val = None
            for i in range(idx,len(candidates)):
                if val != candidates[i]:
                    bucket.append(candidates[i])
                    sums += candidates[i]
                    backtrack(i+1)
                    sums -= candidates[i]
                    val = bucket.pop()

        backtrack(0)
        # for val in visted:
        #     ans.append(list(val))
        return ans