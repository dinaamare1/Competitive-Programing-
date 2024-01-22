class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for idx in range(len(nums)):
            if idx>0 and nums[idx] == nums[idx-1]:
                continue
            l = idx + 1
            r = len(nums)-1
            while l < r:
                sums = nums[idx] + nums[l]+nums[r]
                if sums >0:
                    r -= 1
                elif sums<0:
                    l+= 1
                else:
                    ans.append([nums[idx],nums[l],nums[r]])
                    l+=1
                    while l>0 and l<r and nums[l] == nums[l-1]:
                        l+=1
        return ans
                