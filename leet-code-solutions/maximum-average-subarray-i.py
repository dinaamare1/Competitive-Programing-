class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
       sums = sum(nums[:k])
       maxs = sums/k
       for i in range(len(nums)-k):
           sums -= nums[i]
           sums += nums[i+k]
           maxs = max(sums/k,maxs)
       return maxs