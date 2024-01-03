class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = "_"
        h = 0
        s = 0
        while s < len(nums):
            if nums[s] != "_":
                nums[s],nums[h] = nums[h],nums[s]
                h += 1
            s+=1
        return h

