class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right = -1,len(nums)
        first = 0
        second  = 0
        flag = False
        while left+1<right:
            mid = (left+right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        first = right
        left,right = -1,len(nums)
        while left+1<right:
            mid = (left+right)//2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        second = left
        if target in nums:
            return [first,second]
        return [-1,-1]
     
        