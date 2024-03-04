class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        bucket = []
        def subsets(i):
            if i <= len(nums):
                ans.append(bucket[:])
            for i in range(i,len(nums)):
                bucket.append(nums[i])
                subsets(i+1)
                bucket.pop()
        subsets(0)
        return ans