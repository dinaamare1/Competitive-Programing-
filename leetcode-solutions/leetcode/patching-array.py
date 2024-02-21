class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        sums = 0
        costs = 0
        for val in nums:
            if val > n:
                break
            while val-1> sums:
                costs += 1
                sums += sums+1
            sums += val
        while n>sums:
            costs += 1
            sums += sums+1
        return costs

        