class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0,len(nums) - 1
        while left <right:
            
            mid = (left+right) // 2
            if nums[mid] < nums[left] and nums[mid]<nums[right]:
                left += 1
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid]<nums[right]:
                right = mid - 1
            
        return nums[left]
        