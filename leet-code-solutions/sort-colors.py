class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while nums != sorted(nums):
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
        

        