class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        dic = {}
        for idx,val in enumerate(sorted(nums)):
            if val not in dic:
                dic[val] = idx
        for idx,val in enumerate(nums):
            ans[idx] = dic[val]
        return ans


