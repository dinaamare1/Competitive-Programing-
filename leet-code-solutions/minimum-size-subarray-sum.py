class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       mins = float("inf")
       sums = 0
       l = 0
       for r in range(len(nums)):
           sums += nums[r]
           while sums >= target:
               mins = min(mins,r-l+1)
               sums -= nums[l]
               l+= 1
       if mins == float("inf"):
           return 0
       else:
            return mins