class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
                nums[i] = "_"
        h=0
        s=0
        while s<len(nums):
            if nums[s]!="_":
                nums[h],nums[s]=nums[s],nums[h]
                h+=1
            s+=1
        return len(nums)-count