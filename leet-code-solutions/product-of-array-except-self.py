class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        count = nums.count(0)
        ans = []
        for i in range(len(nums)):
            if nums[i] != 0:
                mul *= nums[i]
        for i in range(len(nums)):
            if count == 1 and nums[i] != 0 or count>1:
                ans.append(0)
            elif nums[i] !=0:
                ans.append(mul//nums[i])
            else:
                ans.append(mul)
        return ans 
        