class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Sortednums = sorted(set(nums))
        maxs = 1
        count = 0 
        if not Sortednums:
            return 0
        for i in range(len(Sortednums)-1):
            if abs(Sortednums[i+1] - Sortednums[i]) == 1:
                count += 1
                maxs = max(maxs,count+1)
            else:
                count = 0
        return maxs