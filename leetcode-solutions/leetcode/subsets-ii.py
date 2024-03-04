class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        bucket = []
        nums.sort()
        def subsets(i):
            if i <= len(nums):
                if bucket[:] not in ans:
                    ans.append(bucket[:])
            for i in range(i,len(nums)):
                bucket.append(nums[i])
                subsets(i+1)
                bucket.pop()
        subsets(0)
        return ans