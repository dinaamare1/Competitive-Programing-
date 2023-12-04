class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums = [str(num) for num in nums]
        ones = "".join(nums)
        ones = ones.split("0")
        maxs = 0
        for i in ones:
            maxs = max(maxs,len(i))
        return maxs

