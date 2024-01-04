class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        count = 0
        l = 0
        r = len(nums)-1
        while l<r:
            if nums[l] + nums[r] < k:
                l+=1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                count += 1
                l+=1
                r-=1
        return count
